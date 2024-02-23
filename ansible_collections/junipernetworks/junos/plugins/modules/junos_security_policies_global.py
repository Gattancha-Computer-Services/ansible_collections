# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
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
The module file for junos_security_policies_global
"""

from __future__ import absolute_import, division, print_function


__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "network",
}

DOCUMENTATION = """
---
module: junos_security_policies_global
version_added: 2.9.0
short_description: Manage global security policy settings on Juniper JUNOS devices
description: This module provides declarative management of global security policy settings on Juniper JUNOS devices
author: Pranav Bhatt (@pranav-bhatt)
requirements:
  - ncclient (>=v0.6.4)
  - xmltodict (>=0.12.0)
notes:
- This module requires the netconf system service be enabled on the device being managed.
- This module works with connection C(netconf).
- See L(the Junos OS Platform Options,https://docs.ansible.com/ansible/latest/network/user_guide/platform_junos.html).
- Tested against JunOS v18.4R1
options:
  config:
    description: A dictionary of security policies
    type: dict
    suboptions:
      default_policy:
        description:
          - Configure the default security policy that defines the actions the device takes on a packet that does not match any user-defined policy.
        choices:
          - deny-all
          - permit-all
        type: str
      policy_rematch:
        description:
          - Enable the device to reevaluate an active session when its associated security policy is modified. The session remains open if it still matches
            the policy that allowed the session initially.
        type: dict
        suboptions:
          enable:
            description:
              - Enable the device to reevaluate an active session when its associated security policy is modified.
                The session remains open if it still matches the policy that allowed the session initially.
            type: bool
          extensive:
            description:
              - When a policy is modified or deleted, extensive option checks if any suitable policy permit to keep these sessions alive.
            type: bool
      policy_stats:
        description:
          - Configure policies statistics.
        type: dict
        suboptions:
          enable:
            description:
              - Enable policies statistics.
            type: bool
          system_wide:
            description:
              - Configure systemwide policies statistics.
            type: bool
      pre_id_default_policy_action:
        description:
          - Configures default policy actions that occur prior to dynamic application identification (AppID) when the packet matches the criteria.
        type: dict
        suboptions:
          log:
            description:
              - Specifies the log details at session close time and session initialization time.
            type: dict
            suboptions:
              session_init:
                description:
                  - Enable logging on session initialization time
                type: bool
              session_close:
                description:
                  - Enable logging on session close time
                type: bool
          session_timeout:
            description:
              - When you update a session, the session timeout is configured, which specifies the session timeout details in seconds.
            type: dict
            suboptions:
              icmp:
                description:
                  - Timeout value for ICMP sessions (seconds)
                type: int
              icmp6:
                description:
                  - Timeout value for ICMP6 sessions (seconds)
                type: int
              ospf:
                description:
                  - Timeout value for OSPF sessions (seconds)
                type: int
              others:
                description:
                  - Timeout value for other sessions (seconds)
                type: int
              tcp:
                description:
                  - Timeout value for TCP sessions (seconds)
                type: int
              udp:
                description:
                  - Timeout value for UDP sessions (seconds)
                type: int
      traceoptions:
        description: A dictionary of security policies
        type: dict
        suboptions:
          file:
            description: A dictionary to configure the trace file options
            type: dict
            suboptions:
              files:
                description:
                  - Maximum number of trace files
                type: int
              match:
                description: Refine the output to include lines that contain the regular expression.
                type: str
              size:
                description: The maximum tracefile size
                type: str
              world_readable:
                description: The world_readable option enables any user to read the file.
                type: bool
              no_world_readable:
                description: Log files can be accessed only by the user who configures the tracing operation.
                type: bool
          flag:
            description:
              - Trace operation to perform.
            choices:
              - all
              - configuration
              - compilation
              - ipc
              - lookup
              - routing-socket
              - rules
            type: str
          no_remote_trace:
            description: Disable remote tracing.
            type: bool
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the JunOS device
        by executing the command B(show security policies).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - rendered
    - gathered
    - parsed
    default: merged
    description:
      - The state the configuration should be left in
      - The states I(rendered), I(gathered) and I(parsed) does not perform any change
        on the device.
      - The state I(rendered) will transform the configuration in C(config) option to
        platform specific CLI commands which will be returned in the I(rendered) key
        within the result. For state I(rendered) active connection to remote host is
        not required.
        behaviour for this module.
      - The state I(replaced) will replace the running configuration with the provided
        configuration
      - The state I(replaced) and state I(overridden) have the same behaviour
      - The state I(gathered) will fetch the running configuration from device and transform
        it into structured data in the format as per the resource module argspec and
        the value is returned in the I(gathered) key within the result.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into JSON format as per the resource module parameters and the
        value is returned in the I(parsed) key within the result. The value of C(running_config)
        option should be the same format as the output of command
        I(show security policies detail) executed on device. For state I(parsed) active
        connection to remote host is not required.
    type: str
"""
EXAMPLES = """
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# default-policy {
#   permit-all;
# }
#
- name: Update the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true,
#         "system_wide": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 3,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {},
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
#   <nc:policy-rematch> <nc:extensive/></nc:policy-rematch><nc:policy-stats>
#   <nc:system-wide>enable</nc:system-wide></nc:policy-stats><nc:pre-id-default-policy>
#   <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp>
#   <nc:others>10</nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy>
#   <nc:traceoptions><nc:file><nc:files>3</nc:files><nc:match>/[A-Z]*/gm</nc:match>
#   <nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag><nc:name>all
#   </nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies></nc:security>"
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }
#
#
# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }

- name: Replace the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
# <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
# <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
# </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
# <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
# </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
# </nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#   no-remote-trace;
#   file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#   flag all;
# }
# default-policy {
#   permit-all;
# }
# policy-rematch extensive;
# policy-stats;
# pre-id-default-policy {
#   then {
#     log {
#       session-init;
#     }
#     session-timeout {
#       icmp 10;
#       others 10;
#     }
#   }
# }

- name: Replace the running configuration with provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "before": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:policies delete="delete"/><nc:policies><nc:default-policy><nc:deny-all/></nc:default-policy>
# <nc:policy-rematch> </nc:policy-rematch><nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy>
# <nc:then><nc:log><nc:session-init/></nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10
# </nc:others></nc:session-timeout></nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file>
# <nc:files>4</nc:files><nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/>
# </nc:file><nc:flag><nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
# </nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
- name: Delete the running configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
# "after": {},
# "before": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# },
# "changed": true,
# "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#               <nc:policies delete="delete"/></nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx# show security policies
#
#
# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx# show security policies
# traceoptions {
#     no-remote-trace;
#     file size 10k files 4 no-world-readable match "/[A-Z]*/gm";
#     flag all;
# }
# default-policy {
#     deny-all;
# }
# policy-rematch;
# policy-stats;
# pre-id-default-policy {
#     then {
#         log {
#             session-init;
#         }
#         session-timeout {
#             icmp 10;
#             others 10;
#         }
#     }
# }
#
- name: Gather the running configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
# "gathered": {
#     "default_policy": "deny-all",
#     "policy_rematch": {
#         "enable": true
#     },
#     "policy_stats": {
#         "enable": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 4,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# }
#
# Using rendered
#
# Before state
# ------------
#
- name: Render the provided configuration
  junipernetworks.junos.junos_security_policies_global:
    config:
      default_policy: deny-all
      policy_rematch:
        enable: true
      policy_stats:
        enable: true
      pre_id_default_policy_action:
        log:
          session_init: true
        session_timeout:
          icmp: 10
          others: 10
      traceoptions:
        file:
          files: 4
          match: /[A-Z]*/gm
          size: 10k
          no_world_readable: true
        flag: all
        no_remote_trace: true
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0"><nc:policies>
#     <nc:default-policy><nc:deny-all/></nc:default-policy><nc:policy-rematch> </nc:policy-rematch>
#     <nc:policy-stats> </nc:policy-stats><nc:pre-id-default-policy><nc:then><nc:log><nc:session-init/>
#     </nc:log><nc:session-timeout><nc:icmp>10</nc:icmp><nc:others>10</nc:others></nc:session-timeout>
#     </nc:then></nc:pre-id-default-policy><nc:traceoptions><nc:file><nc:files>4</nc:files>
#     <nc:match>/[A-Z]*/gm</nc:match><nc:size>10k</nc:size><nc:no-world-readable/></nc:file><nc:flag>
#     <nc:name>all</nc:name></nc:flag><nc:no-remote-trace/></nc:traceoptions></nc:policies>
#     </nc:security>"
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#    <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#       <version>18.4R1-S2.4</version>
#         <security>
#             <policies>
#                 <traceoptions>
#                     <no-remote-trace />
#                     <file>
#                         <size>10k</size>
#                         <files>3</files>
#                         <no-world-readable />
#                         <match>/[A-Z]*/gm</match>
#                     </file>
#                     <flag>
#                         <name>all</name>
#                     </flag>
#                 </traceoptions>
#                 <default-policy>
#                     <permit-all />
#                 </default-policy>
#                 <policy-rematch>
#                     <extensive />
#                 </policy-rematch>
#                 <policy-stats>
#                     <system-wide>enable</system-wide>
#                 </policy-stats>
#                 <pre-id-default-policy>
#                     <then>
#                         <log>
#                             <session-init />
#                         </log>
#                         <session-timeout>
#                             <icmp>10</icmp>
#                             <others>10</others>
#                         </session-timeout>
#                     </then>
#                 </pre-id-default-policy>
#             </policies>
#         </security>
#     </configuration>
# </rpc-reply>
#
#
- name: Parse security policies global running config
  junipernetworks.junos.junos_security_policies_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#     "default_policy": "permit-all",
#     "policy_rematch": {
#         "enable": true,
#         "extensive": true
#     },
#     "policy_stats": {
#         "enable": true,
#         "system_wide": true
#     },
#     "pre_id_default_policy_action": {
#         "log": {
#             "session_init": true
#         },
#         "session_timeout": {
#             "icmp": 10,
#             "others": 10
#         }
#     },
#     "traceoptions": {
#         "file": {
#             "files": 3,
#             "match": "/[A-Z]*/gm",
#             "no_world_readable": true,
#             "size": "10k"
#         },
#         "flag": "all",
#         "no_remote_trace": true
#     }
# }
#
#
"""
RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when state is I(merged), I(replaced), I(overridden), I(deleted)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when state is I(merged), I(replaced), I(overridden) or I(deleted)
  type: list
  sample:
    - "<rpc-reply>
      <configuration>
        <security>
          <policies>
            <default-policy>
              <permit-all />
            </default-policy>
          </policies>
        </security>
      </configuration>
    </rpc-reply>"
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when state is I(rendered)
  type: dict
  sample:
    - "<rpc-reply>
      <configuration>
        <security>
          <policies>
            <default-policy>
              <permit-all />
            </default-policy>
          </policies>
        </security>
      </configuration>
    </rpc-reply>"
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when state is I(gathered)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when state is I(parsed)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
"""


from ansible.module_utils.basic import AnsibleModule

from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.argspec.security_policies_global.security_policies_global import (
    Security_policies_globalArgs,
)
from ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.security_policies_global.security_policies_global import (
    Security_policies_global,
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

    module = AnsibleModule(
        argument_spec=Security_policies_globalArgs.argument_spec,
        required_if=required_if,
        supports_check_mode=True,
    )

    result = Security_policies_global(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
