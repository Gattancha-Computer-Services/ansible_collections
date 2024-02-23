# -*- coding: utf-8 -*-
# © Copyright 2020 Dell Inc. or its subsidiaries. All Rights Reserved
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for sonic_vrfs
"""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = """
---
module: sonic_vrfs
version_added: 1.0.0
notes:
- Tested against Enterprise SONiC Distribution by Dell Technologies.
- Supports C(check_mode).
short_description: Manage VRFs and associate VRFs to interfaces such as, Eth, LAG, VLAN, and loopback
description: Manages VRF and VRF interface attributes in Enterprise SONiC Distribution by Dell Technologies.
author: Abirami N (@abirami-n)
options:
  config:
    description: A list of VRF configurations.
    type: list
    elements: dict
    suboptions:
      name:
        type: str
        description: The name of the VRF interface.
        required: true
      members:
        type: dict
        description: Holds a dictionary mapping of list of interfaces linked to a VRF interface.
        suboptions:
          interfaces:
            type: list
            elements: dict
            description: List of interface names that are linked to a specific VRF interface.
            suboptions:
              name:
                type: str
                description: The name of the physical interface.
  state:
    description: "The state of the configuration after module completion."
    type: str
    choices:
    - merged
    - deleted
    default: merged
"""
EXAMPLES = """
# Using deleted
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/3
#                    Eth1/14
#                    Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#                    Eth1/6
#
- name: Configuring vrf deleted state
  dellemc.enterprise_sonic.sonic_vrfs:
    config:
     - name: Vrfcheck4
       members:
         interfaces:
           - name: Eth1/6
     - name: Vrfcheck3
       members:
         interfaces:
           - name: Eth1/3
           - name: Eth1/14
    state: deleted
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#
#
# Using merged
#
# Before state:
# -------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/16
#                    Eth1/17
#Vrfcheck4
#
- name: Configuring vrf merged state
  dellemc.enterprise_sonic.sonic_vrfs:
    config:
     - name: Vrfcheck4
       members:
         interfaces:
           - name: Eth1/5
           - name: Eth1/6
     - name: Vrfcheck3
       members:
         interfaces:
           - name: Eth1/3
           - name: Eth1/14
    state: merged
#
# After state:
# ------------
#
#show ip vrf
#VRF-NAME            INTERFACES
#----------------------------------------------------------------
#Vrfcheck1
#Vrfcheck2
#Vrfcheck3           Eth1/3
#                    Eth1/14
#                    Eth1/16
#                    Eth1/17
#Vrfcheck4           Eth1/5
#                    Eth1/6
#
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
after:
  description: The resulting configuration model invocation.
  returned: when changed
  type: list
  sample: >
    The configuration returned is always in the same format
    of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['command 1', 'command 2', 'command 3']
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.argspec.vrfs.vrfs import VrfsArgs
from ansible_collections.dellemc.enterprise_sonic.plugins.module_utils.network.sonic.config.vrfs.vrfs import Vrfs


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(argument_spec=VrfsArgs.argument_spec,
                           supports_check_mode=True)

    result = Vrfs(module).execute_module()
    module.exit_json(**result)


if __name__ == '__main__':
    main()