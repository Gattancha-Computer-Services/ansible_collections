# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
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
The module file for nxos_l2_interfaces
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: nxos_l2_interfaces
short_description: L2 interfaces resource module
description: This module manages Layer-2 interfaces attributes of NX-OS Interfaces.
version_added: 1.0.0
author: Trishna Guha (@trishnaguha)
notes:
- Tested against NXOS 7.3.(0)D1(1) on VIRL
- Unsupported for Cisco MDS
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the NX-OS device
      by executing the command B(show running-config | section ^interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A dictionary of Layer-2 interface options
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Full name of interface, i.e. Ethernet1/1.
        type: str
        required: true
      access:
        description:
        - Switchport mode access command to configure the interface as a Layer-2 access.
        type: dict
        suboptions:
          vlan:
            description:
            - Configure given VLAN in access port. It's used as the access VLAN ID.
            type: int
      trunk:
        description:
        - Switchport mode trunk command to configure the interface as a Layer-2 trunk.
        type: dict
        suboptions:
          native_vlan:
            description:
            - Native VLAN to be configured in trunk port. It is used as the trunk
              native VLAN ID.
            type: int
          allowed_vlans:
            description:
            - List of allowed VLANs in a given trunk port. These are the only VLANs
              that will be configured on the trunk.
            type: str
      mode:
        description:
        - Mode in which interface needs to be configured.
        - Access mode is not shown in interface facts, so idempotency will not be
          maintained for switchport mode access and every time the output will come
          as changed=True.
        type: str
        choices:
        - dot1q-tunnel
        - access
        - trunk
        - fex-fabric
        - fabricpath
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
"""

EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
#   switchport trunk native vlan 20
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Merge provided configuration with device configuration
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 10
        allowed_vlans: 2,4,15
    - name: Ethernet1/2
      access:
        vlan: 30
    state: merged

# Task Output
# -----------
#
# before:
# - name: Loopback999
# - name: Ethernet1/2
# - name: mgmt0
# - name: Ethernet1/1
# commands:
# - interface Ethernet1/1
# - switchport trunk allowed vlan 2,4,15
# - switchport trunk native vlan 10
# - interface Ethernet1/2
# - switchport access vlan 30
# after:
# - name: Ethernet1/1
#   trunk:
#     allowed_vlans: 2,4,15
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0
# - name: Loopback999

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   switchport trunk native vlan 10
#   switchport trunk allowed vlans 2,4,15
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using replaced

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   switchport trunk native vlan 10
#   switchport trunk allowed vlans 2,4,15
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Replace device configuration of specified L2 interfaces with provided configuration.
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 20
        allowed_vlans: 5-10, 15
    state: replaced

# Task Output
# -----------
#
# before:
# - name: Ethernet1/1
#   trunk:
#     allowed_vlans: 2,4,15
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0
# commands:
# - interface Ethernet1/1
# - no switchport trunk native vlan
# - switchport trunk allowed vlan 5-10,15
# - switchport trunk native vlan 20
# after:
# - name: Ethernet1/1
#   trunk:
#     allowed_vlans: 5-10,15
#     native_vlan: 20
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   switchport trunk native vlan 20
#   switchport trunk allowed vlan 5-10,15
# interface Ethernet1/2
#   switchport trunk native vlan 20
#   switchport mode trunk
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using overridden

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   switchport trunk native vlan 20
#   switchport trunk allowed vlan 5-10,15
# interface Ethernet1/2
#   switchport trunk native vlan 20
#   switchport mode trunk
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Override device configuration with provided configuration.
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/2
      access:
        vlan: 30
    state: overridden

# Task Output
# -----------
#
# before:
# - name: Ethernet1/1
#   trunk:
#     allowed_vlans: 5,6,7,8,9,10,15
#     native_vlan: 20
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0
# commands:
# - interface Ethernet1/1
# - no switchport trunk allowed vlan
# - no switchport trunk native vlan
# after:
# - name: Ethernet1/1
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config


# Using deleted

# Before state:
# -------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
#   switchport trunk native vlan 10
#   switchport trunk allowed vlan 2,4,15
# interface Ethernet1/2
#   switchport access vlan 30
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

- name: Delete L2 attributes of given interfaces (Note This won't delete the interface
    itself).
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
    - name: Ethernet1/2
    state: deleted

# Task Output
# -----------
#
# before:
# - name: Ethernet1/1
#   trunk:
#     allowed_vlans: 2,4,15
#     native_vlan: 10
# - access:
#     vlan: 30
#   name: Ethernet1/2
# - name: mgmt0
# commands:
# - interface Ethernet1/1
# - no switchport trunk allowed vlan
# - no switchport trunk native vlan
# - interface Ethernet1/2
# - no switchport access vlan
# after:
# - name: Ethernet1/1
# - name: Ethernet1/2
# - name: mgmt0

# After state:
# ------------
#
# switch# show running-config | section interface
# interface Ethernet1/1
# interface Ethernet1/2
# interface mgmt0
#   ip address dhcp
#   ipv6 address auto-config

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_l2_interfaces:
    config:
    - name: Ethernet1/1
      trunk:
        native_vlan: 10
        allowed_vlans: 2,4,15
    - name: Ethernet1/2
      access:
        vlan: 30
    - name: Ethernet1/3
      trunk:
        native_vlan: 20
        allowed_vlans: 5-10, 15
    state: rendered

# Task Output
# -----------
#
# rendered:
# - interface Ethernet1/1
# - switchport trunk allowed vlan 2,4,15
# - switchport trunk native vlan 10
# - interface Ethernet1/2
# - switchport access vlan 30
# - interface Ethernet1/3
# - switchport trunk allowed vlan 5-10,15
# - switchport trunk native vlan 20

# Using parsed

# parsed.cfg
# ------------
#
# interface Ethernet1/800
#   switchport access vlan 18
#   switchport trunk allowed vlan 210
# interface Ethernet1/801
#   switchport trunk allowed vlan 2,4,15

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_l2_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output
# -----------
#
# parsed:
#  - name: Ethernet1/800
#    access:
#      vlan: 18
#    trunk:
#      allowed_vlans: "210"
#  - name: Ethernet1/801
#    trunk:
#      allowed_vlans: "2,4,15"

# Using gathered

# Before state:
# -------------
#
# switch# sh running-config | section ^interface
# interface Ethernet1/1
#   switchport access vlan 6
#   switchport trunk allowed vlan 200
# interface Ethernet1/2
#   switchport trunk native vlan 10

- name: Gather l2_interfaces facts from the device using nxos_l2_interfaces
  cisco.nxos.nxos_l2_interfaces:
    state: gathered

# Task output
# -----------
#
# gathered:
#  - name: "Ethernet1/1"
#    access:
#      vlan: 6
#    trunk:
#      allowed_vlans: "200"
#  - name: "Ethernet1/2"
#    trunk:
#      native_vlan: 10
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "interface Ethernet1/1"
    - "switchport trunk allowed vlan 2,4,15"
    - "switchport trunk native vlan 10"
    - "interface Ethernet1/2"
    - "switchport access vlan 30"
    - "interface Ethernet1/3"
    - "switchport trunk allowed vlan 5,6,7,8,9,10,15"
    - "switchport trunk native vlan 20"
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.l2_interfaces.l2_interfaces import (
    L2_interfacesArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.l2_interfaces.l2_interfaces import (
    L2_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=L2_interfacesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = L2_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
