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
The module file for iosxr_static_routes
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type


DOCUMENTATION = """
module: iosxr_static_routes
short_description: Resource module to configure static routes.
description:
- This module manages static routes on devices running Cisco IOS-XR.
version_added: 1.0.0
author: Nilashish Chakraborty (@NilashishC)
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the IOS-XR device
      by executing the command B(show running-config router static).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A dictionary of static route options.
    type: list
    elements: dict
    suboptions:
      vrf:
        description:
        - The VRF to which the static route(s) belong.
        type: str
      address_families:
        description: A dictionary specifying the address family to which the static
          route(s) belong.
        type: list
        elements: dict
        suboptions:
          afi:
            description:
            - Specifies the top level address family indicator.
            type: str
            choices:
            - ipv4
            - ipv6
            required: true
          safi:
            description:
            - Specifies the subsequent address family indicator.
            type: str
            choices:
            - unicast
            - multicast
            required: true
          routes:
            description: A dictionary that specifies the static route configurations.
            elements: dict
            type: list
            suboptions:
              dest:
                description:
                - An IPv4 or IPv6 address in CIDR notation that specifies the destination
                  network for the static route.
                type: str
                required: true
              next_hops:
                description:
                - Next hops to the specified destination.
                type: list
                elements: dict
                suboptions:
                  forward_router_address:
                    description:
                    - The IP address of the next hop that can be used to reach the
                      destination network.
                    type: str
                  interface:
                    description:
                    - The interface to use to reach the destination.
                    type: str
                  dest_vrf:
                    description:
                    - The destination VRF.
                    type: str
                  admin_distance:
                    description:
                    - The administrative distance for this static route.
                    - Refer to vendor documentation for valid values.
                    type: int
                  metric:
                    description:
                    - Specifes the metric for this static route.
                    - Refer to vendor documentation for valid values.
                    type: int
                  description:
                    description:
                    - Specifies the description for this static route.
                    type: str
                  vrflabel:
                    description:
                    - Specifies the VRF label for this static route.
                    - Refer to vendor documentation for valid values.
                    type: int
                  tag:
                    description:
                    - Specifies a numeric tag for this static route.
                    - Refer to vendor documentation for valid values.
                    type: int
                  track:
                    description:
                    - Specifies the object to be tracked.
                    - This enables object tracking for static routes.
                    type: str
                  tunnel_id:
                    description:
                    - Specifies a tunnel id for the route.
                    - Refer to vendor documentation for valid values.
                    type: int
  state:
    description:
    - The state the configuration should be left in.
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

# Before state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:46:30.089 UTC
# % No such configuration item(s)
#
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_static_routes:
    config:
    - address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.16/28
          next_hops:
          - forward_router_address: 192.0.2.10
            interface: FastEthernet0/0/0/1
            description: LAB
            metric: 120
            tag: 10

          - interface: FastEthernet0/0/0/5
            track: ip_sla_1

        - dest: 192.0.2.32/28
          next_hops:
          - forward_router_address: 192.0.2.11
            admin_distance: 100

      - afi: ipv6
        safi: unicast
        routes:
        - dest: 2001:db8:1000::/36
          next_hops:
          - interface: FastEthernet0/0/0/7
            description: DC

          - interface: FastEthernet0/0/0/8
            forward_router_address: 2001:db8:2000:2::1

    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.12
            description: DEV
            dest_vrf: test_1

        - dest: 192.0.2.80/28
          next_hops:
          - interface: FastEthernet0/0/0/2
            forward_router_address: 192.0.2.14
            dest_vrf: test_1
            track: ip_sla_2
            vrflabel: 124
    state: merged

# After state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

# Using merged to update existing static routes

# Before state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Update existing static routes configuration using merged
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.12
            vrflabel: 2301
            dest_vrf: test_1

        - dest: 192.0.2.80/28
          next_hops:
          - interface: FastEthernet0/0/0/2
            forward_router_address: 192.0.2.14
            dest_vrf: test_1
            description: rt_test_1
    state: merged

# After state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV vrflabel 2301
#    192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 description rt_test_1 track ip_sla_2 vrflabel 124
#   !
#  !
# !

# Using replaced to replace all next hop entries for a single destination network

# Before state
# --------------

# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Replace device configurations of static routes with provided configurations
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.15
            interface: FastEthernet0/0/0/3
            description: DEV_NEW
            dest_vrf: dev_test_2
    state: replaced

# After state
# ------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:04:07.085 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf dev_test_2 FastEthernet0/0/0/3 192.0.2.15 description DEV_NEW
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

# Using overridden to override all static route entries on the device

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Overridde all static routes configuration with provided configuration
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_NEW
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.15
            interface: FastEthernet0/0/0/3
            description: DEV1
      - afi: ipv6
        safi: unicast
        routes:
        - dest: 2001:db8:3000::/36
          next_hops:
          - interface: FastEthernet0/0/0/4
            forward_router_address: 2001:db8:2000:2::2
            description: PROD1
            track: ip_sla_1
    state: overridden

# After state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:07:41.516 UTC
# router static
#  vrf DEV_NEW
#   address-family ipv4 unicast
#    192.0.2.48/28 FastEthernet0/0/0/3 192.0.2.15 description DEV1
#   !
#   address-family ipv6 unicast
#    2001:db8:3000::/36 FastEthernet0/0/0/4 2001:db8:2000:2::2 description PROD1 track ip_sla_1
#   !
#  !
# !

# Using deleted to delete all destination network entries under a single AFI

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Delete all destination network entries under a single AFI
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
    state: deleted

# After state
# ------------

# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:16:41.464 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#  !
# !

# Using deleted to remove all static route entries from the device

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Delete static routes configuration
  cisco.iosxr.iosxr_static_routes:
    state: deleted

# After state
# ------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:50:43.038 UTC
# % No such configuration item(s)

# Using gathered to gather static route facts from the device

- name: Gather static routes facts from the device using iosxr_static_routes module
  cisco.iosxr.iosxr_static_routes:
    state: gathered

# Task output (redacted)
# -----------------------
# "gathered": [
#    {
#        "address_families": [
#            {
#                "afi": "ipv4",
#                "routes": [
#                    {
#                        "dest": "192.0.2.16/28",
#                        "next_hops": [
#                            {
#                                "description": "LAB",
#                                "forward_router_address": "192.0.2.10",
#                                "interface": "FastEthernet0/0/0/1",
#                                "metric": 120,
#                                "tag": 10
#                            },
#                            {
#                                "interface": "FastEthernet0/0/0/5",
#                                "track": "ip_sla_1"
#                            }
#                        ]
#                    },
#                    {
#                        "dest": "192.0.2.32/28",
#                        "next_hops": [
#                            {
#                                "admin_distance": 100,
#                                "forward_router_address": "192.0.2.11"
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            },
#            {
#                "afi": "ipv6",
#                "routes": [
#                    {
#                        "dest": "2001:db8:1000::/36",
#                        "next_hops": [
#                            {
#                                "description": "DC",
#                                "interface": "FastEthernet0/0/0/7"
#                            },
#                            {
#                                "forward_router_address": "2001:db8:2000:2::1",
#                                "interface": "FastEthernet0/0/0/8"
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            }
#        ]
#    },
#    {
#        "address_families": [
#            {
#                "afi": "ipv4",
#                "routes": [
#                    {
#                        "dest": "192.0.2.48/28",
#                        "next_hops": [
#                            {
#                                "description": "DEV",
#                                "dest_vrf": "test_1",
#                                "forward_router_address": "192.0.2.12"
#                            },
#                            {
#                                "forward_router_address": "192.0.3.24",
#                                "interface": "GigabitEthernet0/0/0/1",
#                                "vrflabel": 2302
#                            }
#                        ]
#                    },
#                    {
#                        "dest": "192.0.2.80/28",
#                        "next_hops": [
#                            {
#                                "dest_vrf": "test_1",
#                                "forward_router_address": "192.0.2.14",
#                                "interface": "FastEthernet0/0/0/2",
#                                "track": "ip_sla_2",
#                                "vrflabel": 124
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            }
#        ],
#        "vrf": "DEV_SITE"
#    }
#  ]

# Using rendered

- name: Render platform specific commands (without connecting to the device)
  cisco.iosxr.iosxr_static_routes:
  config:
  - vrf: DEV_SITE
    address_families:
    - afi: ipv4
      safi: unicast
      routes:
      - dest: 192.0.2.48/28
        next_hops:
        - forward_router_address: 192.0.2.12
          description: DEV
          dest_vrf: test_1

      - dest: 192.0.2.80/28
        next_hops:
        - interface: FastEthernet0/0/0/2
          forward_router_address: 192.0.2.14
          dest_vrf: test_1
          track: ip_sla_2
          vrflabel: 124

# Task Output (redacted)
# -----------------------
# "rendered": [
#    "router static"s,
#    "vrf DEV_SITE",
#    "address-family ipv4 unicast",
#    "192.0.2.48/28 vrf test_1 192.0.2.12 description DEV",
#    "192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 track ip_sla_2 vrflabel 124"

# Using parsed

# parsed.cfg
# ------------
# Fri Nov 29 21:10:41.896 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Use parsed state to convert externally supplied device specific static routes
    commands to structured format
  cisco.iosxr.iosxr_static_routes:
    running_config: "{{ lookup('file', '../../fixtures/parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# "parsed": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "192.0.2.16/28",
#                            "next_hops": [
#                                {
#                                    "description": "LAB",
#                                    "forward_router_address": "192.0.2.10",
#                                    "interface": "FastEthernet0/0/0/1",
#                                    "metric": 120,
#                                    "tag": 10
#                                },
#                                {
#                                    "interface": "FastEthernet0/0/0/5",
#                                    "track": "ip_sla_1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "forward_router_address": "192.0.2.11"
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "description": "DC",
#                                    "interface": "FastEthernet0/0/0/7"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1",
#                                    "interface": "FastEthernet0/0/0/8"
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "192.0.2.48/28",
#                            "next_hops": [
#                                {
#                                    "description": "DEV",
#                                    "dest_vrf": "test_1",
#                                    "forward_router_address": "192.0.2.12"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "192.0.2.80/28",
#                            "next_hops": [
#                                {
#                                    "dest_vrf": "test_1",
#                                    "forward_router_address": "192.0.2.14",
#                                    "interface": "FastEthernet0/0/0/2",
#                                    "track": "ip_sla_2",
#                                    "vrflabel": 124
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                }
#            ],
#            "vrf": "DEV_SITE"
#        }
#    ]
# }
"""
RETURN = """
before:
  description: The configuration prior to the model invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The resulting configuration model invocation.
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
    - router static
    - vrf dev_site
    - address-family ipv4 unicast
    - 192.0.2.48/28 192.0.2.12 FastEthernet0/0/0/1 track ip_sla_10 description dev1
    - address-family ipv6 unicast
    - no 2001:db8:1000::/36
    - 2001:db8:3000::/36 2001:db8:2000:2::2 FastEthernet0/0/0/4 track ip_sla_11 description prod1
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.argspec.static_routes.static_routes import (
    Static_routesArgs,
)
from ansible_collections.cisco.iosxr.plugins.module_utils.network.iosxr.config.static_routes.static_routes import (
    Static_routes,
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
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Static_routesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Static_routes(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
