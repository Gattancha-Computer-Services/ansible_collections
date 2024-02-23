# -*- coding: utf-8 -*-
# © 2020 Nokia
# Licensed under the GNU General Public License v3.0 only
# SPDX-License-Identifier: GPL-3.0-only

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
---
module: netbox_console_server_port_template
short_description: Create, update or delete console server port templates within NetBox
description:
  - Creates, updates or removes console server port templates from NetBox
notes:
  - Tags should be defined as a YAML list
  - This should be ran with connection C(local) and hosts C(localhost)
author:
  - Tobias Groß (@toerb)
requirements:
  - pynetbox
version_added: '0.2.3'
extends_documentation_fragment:
  - netbox.netbox.common
options:
  data:
    type: dict
    required: true
    description:
      - Defines the console server port template configuration
    suboptions:
      device_type:
        description:
          - The device type the console server port template is attached to
        required: true
        type: raw
      name:
        description:
          - The name of the console server port template
        required: true
        type: str
      type:
        description:
          - The type of the console server port template
        choices:
          - de-9
          - db-25
          - rj-11
          - rj-12
          - rj-45
          - usb-a
          - usb-b
          - usb-c
          - usb-mini-a
          - usb-mini-b
          - usb-micro-a
          - usb-micro-b
          - other
        required: false
        type: str
"""

EXAMPLES = r"""
- name: "Test NetBox modules"
  connection: local
  hosts: localhost
  gather_facts: False

  tasks:
    - name: Create console server port template within NetBox with only required information
      netbox.netbox.netbox_console_server_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Server Port Template
          device_type: Test Device Type
        state: present

    - name: Update console server port template with other fields
      netbox.netbox.netbox_console_server_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Server Port Template
          device_type: Test Device Type
          type: iec-60320-c6
        state: present

    - name: Delete console server port template within netbox
      netbox.netbox.netbox_console_server_port_template:
        netbox_url: http://netbox.local
        netbox_token: thisIsMyToken
        data:
          name: Test Console Server Port Template
          device_type: Test Device Type
        state: absent
"""

RETURN = r"""
console_server_port_template:
  description: Serialized object as created or already existent within NetBox
  returned: success (when I(state=present))
  type: dict
msg:
  description: Message indicating failure or info about what has been achieved
  returned: always
  type: str
"""

from ansible_collections.netbox.netbox.plugins.module_utils.netbox_utils import (
    NetboxAnsibleModule,
    NETBOX_ARG_SPEC,
)
from ansible_collections.netbox.netbox.plugins.module_utils.netbox_dcim import (
    NetboxDcimModule,
    NB_CONSOLE_SERVER_PORT_TEMPLATES,
)
from copy import deepcopy


def main():
    """
    Main entry point for module execution
    """
    argument_spec = deepcopy(NETBOX_ARG_SPEC)
    argument_spec.update(
        dict(
            data=dict(
                type="dict",
                required=True,
                options=dict(
                    device_type=dict(required=True, type="raw"),
                    name=dict(required=True, type="str"),
                    type=dict(
                        required=False,
                        choices=[
                            "de-9",
                            "db-25",
                            "rj-11",
                            "rj-12",
                            "rj-45",
                            "usb-a",
                            "usb-b",
                            "usb-c",
                            "usb-mini-a",
                            "usb-mini-b",
                            "usb-micro-a",
                            "usb-micro-b",
                            "other",
                        ],
                        type="str",
                    ),
                ),
            ),
        )
    )

    required_if = [
        ("state", "present", ["device_type", "name"]),
        ("state", "absent", ["device_type", "name"]),
    ]

    module = NetboxAnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True, required_if=required_if
    )

    netbox_console_server_port_template = NetboxDcimModule(
        module, NB_CONSOLE_SERVER_PORT_TEMPLATES
    )
    netbox_console_server_port_template.run()


if __name__ == "__main__":  # pragma: no cover
    main()
