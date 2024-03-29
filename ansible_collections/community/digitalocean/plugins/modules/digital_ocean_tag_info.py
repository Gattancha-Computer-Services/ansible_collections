# -*- coding: utf-8 -*-
# Copyright: (c) 2018, Ansible Project
# Copyright: (c) 2018, Abhijeet Kasurde <akasurde@redhat.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
---
module: digital_ocean_tag_info
short_description: Gather information about DigitalOcean tags
description:
    - This module can be used to gather information about DigitalOcean provided tags.
    - This module was called C(digital_ocean_tag_facts) before Ansible 2.9. The usage did not change.
author: "Abhijeet Kasurde (@Akasurde)"
options:
  tag_name:
    description:
     - Tag name that can be used to identify and reference a tag.
    required: false
    type: str
requirements:
  - "python >= 2.6"
extends_documentation_fragment:
- community.digitalocean.digital_ocean.documentation

"""


EXAMPLES = r"""
- name: Gather information about all tags
  community.digitalocean.digital_ocean_tag_info:
    oauth_token: "{{ oauth_token }}"

- name: Gather information about tag with given name
  community.digitalocean.digital_ocean_tag_info:
    oauth_token: "{{ oauth_token }}"
    tag_name: "extra_awesome_tag"

- name: Get resources from tag name
  community.digitalocean.digital_ocean_tag_info:
  register: resp_out
- set_fact:
    resources: "{{ item.resources }}"
  loop: "{{ resp_out.data | community.general.json_query(name) }}"
  vars:
    name: "[?name=='extra_awesome_tag']"
- debug:
    var: resources
"""


RETURN = r"""
data:
    description: DigitalOcean tag information
    returned: success
    type: list
    elements: dict
    sample: [
        {
            "name": "extra-awesome",
            "resources": {
            "droplets": {
                "count": 1,
                ...
                }
            }
        },
    ]
"""

from traceback import format_exc
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.community.digitalocean.plugins.module_utils.digital_ocean import (
    DigitalOceanHelper,
)
from ansible.module_utils._text import to_native


def core(module):
    tag_name = module.params.get("tag_name", None)
    rest = DigitalOceanHelper(module)

    base_url = "tags"
    if tag_name is not None:
        response = rest.get("%s/%s" % (base_url, tag_name))
        status_code = response.status_code

        if status_code != 200:
            module.fail_json(msg="Failed to retrieve tags for DigitalOcean")

        tag = [response.json["tag"]]
    else:
        tag = rest.get_paginated_data(base_url=base_url + "?", data_key_name="tags")

    module.exit_json(changed=False, data=tag)


def main():
    argument_spec = DigitalOceanHelper.digital_ocean_argument_spec()
    argument_spec.update(
        tag_name=dict(type="str", required=False),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    if module._name in (
        "digital_ocean_tag_facts",
        "community.digitalocean.digital_ocean_tag_facts",
    ):
        module.deprecate(
            "The 'digital_ocean_tag_facts' module has been renamed to 'digital_ocean_tag_info'",
            version="2.0.0",
            collection_name="community.digitalocean",
        )  # was Ansible 2.13

    try:
        core(module)
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=format_exc())


if __name__ == "__main__":
    main()
