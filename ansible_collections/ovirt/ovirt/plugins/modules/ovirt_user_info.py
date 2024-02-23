# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 Red Hat, Inc.
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: ovirt_user_info
short_description: Retrieve information about one or more oVirt/RHV users
version_added: "1.0.0"
author: "Ondra Machacek (@machacekondra)"
description:
    - "Retrieve information about one or more oVirt/RHV users."
    - This module was called C(ovirt_user_facts) before Ansible 2.9, returning C(ansible_facts).
      Note that the M(ovirt.ovirt.ovirt_user_info) module no longer returns C(ansible_facts)!
notes:
    - "This module returns a variable C(ovirt_users), which
       contains a list of users. You need to register the result with
       the I(register) keyword to use it."
options:
    pattern:
        description:
            - "Search term which is accepted by oVirt/RHV search backend."
            - "For example to search user X use following pattern: name=X"
        type: str
    follow:
        description:
            - List of linked entities, which should be fetched along with the main entity.
            - This parameter replaces usage of C(fetch_nested) and C(nested_attributes).
            - "All follow parameters can be found at following url: https://ovirt.github.io/ovirt-engine-api-model/master/#types/user/links_summary"
        type: list
        version_added: 1.5.0
        elements: str
        aliases: ['follows']
extends_documentation_fragment: ovirt.ovirt.ovirt_info
'''

EXAMPLES = '''
# Examples don't contain auth parameter for simplicity,
# look at ovirt_auth module to see how to reuse authentication:

# Gather information about all users which first names start with C(john):
- ovirt.ovirt.ovirt_user_info:
    pattern: name=john*
  register: result
- ansible.builtin.debug:
    msg: "{{ result.ovirt_users }}"
'''

RETURN = '''
ovirt_users:
    description: "List of dictionaries describing the users. User attributes are mapped to dictionary keys,
                  all users attributes can be found at following url: http://ovirt.github.io/ovirt-engine-api-model/master/#types/user."
    returned: On success.
    type: list
'''

import traceback

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ovirt.ovirt.plugins.module_utils.ovirt import (
    check_sdk,
    create_connection,
    get_dict_of_struct,
    ovirt_info_full_argument_spec,
)


def main():
    argument_spec = ovirt_info_full_argument_spec(
        pattern=dict(default='', required=False),
    )
    module = AnsibleModule(
        argument_spec,
        supports_check_mode=True,
    )
    check_sdk(module)
    if module.params['fetch_nested'] or module.params['nested_attributes']:
        module.deprecate(
            "The 'fetch_nested' and 'nested_attributes' are deprecated please use 'follow' parameter",
            version='3.0.0',
            collection_name='ovirt.ovirt'
        )

    try:
        auth = module.params.pop('auth')
        connection = create_connection(auth)
        users_service = connection.system_service().users_service()
        users = users_service.list(
            search=module.params['pattern'],
            follow=",".join(module.params['follow'])
        )
        result = dict(
            ovirt_users=[
                get_dict_of_struct(
                    struct=c,
                    connection=connection,
                    fetch_nested=module.params.get('fetch_nested'),
                    attributes=module.params.get('nested_attributes'),
                ) for c in users
            ],
        )
        module.exit_json(changed=False, **result)
    except Exception as e:
        module.fail_json(msg=str(e), exception=traceback.format_exc())
    finally:
        connection.close(logout=auth.get('token') is None)


if __name__ == '__main__':
    main()
