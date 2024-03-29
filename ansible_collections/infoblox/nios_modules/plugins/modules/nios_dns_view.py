# Copyright (c) 2018-2019 Red Hat, Inc.
# Copyright (c) 2020 Infoblox, Inc.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: nios_dns_view
author: "Peter Sprygada (@privateip)"
short_description: Configure Infoblox NIOS DNS views
version_added: "1.0.0"
description:
  - Adds and/or removes instances of DNS view objects from
    Infoblox NIOS servers.  This module manages NIOS C(view) objects
    using the Infoblox WAPI interface over REST.
  - Updates instances of DNS view object from Infoblox NIOS servers.
requirements:
  - infoblox-client
extends_documentation_fragment: infoblox.nios_modules.nios
notes:
    - This module supports C(check_mode).
options:
  name:
    description:
      - Specifies the fully qualified hostname to add or remove from
        the system. User can also update the hostname as it is possible
        to pass a dict containing I(new_name), I(old_name). See examples.
    required: true
    aliases:
      - view
    type: str
  network_view:
    description:
      - Specifies the name of the network view to assign the configured
        DNS view to.  The network view must already be configured on the
        target system.
    default: default
    type: str
  extattrs:
    description:
      - Allows for the configuration of Extensible Attributes on the
        instance of the object.  This argument accepts a set of key / value
        pairs for configuration.
    type: dict
  comment:
    description:
      - Configures a text string comment to be associated with the instance
        of this object.  The provided text string will be configured on the
        object instance.
    type: str
  state:
    description:
      - Configures the intended state of the instance of the object on
        the NIOS server.  When this value is set to C(present), the object
        is configured on the device and when this value is set to C(absent)
        the value is removed (if necessary) from the device.
    default: present
    choices:
      - present
      - absent
    type: str

'''

EXAMPLES = '''
- name: Configure a new dns view instance
  infoblox.nios_modules.nios_dns_view:
    name: ansible-dns
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Update the comment for dns view
  infoblox.nios_modules.nios_dns_view:
    name: ansible-dns
    comment: this is an example comment
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Remove the dns view instance
  infoblox.nios_modules.nios_dns_view:
    name: ansible-dns
    state: absent
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local

- name: Update the dns view instance
  infoblox.nios_modules.nios_dns_view:
    name: {new_name: ansible-dns-new, old_name: ansible-dns}
    state: present
    provider:
      host: "{{ inventory_hostname_short }}"
      username: admin
      password: admin
  connection: local
'''

RETURN = ''' # '''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.api import WapiModule
from ..module_utils.api import NIOS_DNS_VIEW
from ..module_utils.api import normalize_ib_spec


def main():
    ''' Main entry point for module execution
    '''
    ib_spec = dict(
        name=dict(required=True, aliases=['view'], ib_req=True),
        network_view=dict(default='default', ib_req=True),

        extattrs=dict(type='dict'),
        comment=dict()
    )

    argument_spec = dict(
        provider=dict(required=True),
        state=dict(default='present', choices=['present', 'absent'])
    )

    argument_spec.update(normalize_ib_spec(ib_spec))
    argument_spec.update(WapiModule.provider_spec)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True)

    wapi = WapiModule(module)
    result = wapi.run(NIOS_DNS_VIEW, ib_spec)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
