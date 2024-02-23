# -*- coding: utf-8 -*-

# Copyright: (c) 2014, Paul Durivage <paul.durivage@rackspace.com>
# Copyright: (c) 2014, Trond Hindenes <trond@hindenes.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r'''
---
module: win_feature
short_description: Installs and uninstalls Windows Features on Windows Server
description:
    - Installs or uninstalls Windows Roles or Features on Windows Server.
    - This module uses the Add/Remove-WindowsFeature Cmdlets on Windows 2008 R2
      and Install/Uninstall-WindowsFeature Cmdlets on Windows 2012, which are not available on client os machines.
options:
  name:
    description:
      - Names of roles or features to install as a single feature or a comma-separated list of features.
      - To list all available features use the PowerShell command C(Get-WindowsFeature).
    type: list
    elements: str
    required: yes
  state:
    description:
      - State of the features or roles on the system.
    type: str
    choices: [ absent, present ]
    default: present
  include_sub_features:
    description:
      - Adds all subfeatures of the specified feature.
    type: bool
    default: no
  include_management_tools:
    description:
      - Adds the corresponding management tools to the specified feature.
      - Not supported in Windows 2008 R2 and will be ignored.
    type: bool
    default: no
  source:
    description:
      - Specify a source to install the feature from.
      - Not supported in Windows 2008 R2 and will be ignored.
      - Can either be C({driveletter}:\sources\sxs) or C(\\{IP}\share\sources\sxs).
    type: str
seealso:
- module: chocolatey.chocolatey.win_chocolatey
- module: ansible.windows.win_package
author:
    - Paul Durivage (@angstwad)
    - Trond Hindenes (@trondhindenes)
'''

EXAMPLES = r'''
- name: Install IIS (Web-Server only)
  ansible.windows.win_feature:
    name: Web-Server
    state: present

- name: Install IIS (Web-Server and Web-Common-Http)
  ansible.windows.win_feature:
    name:
    - Web-Server
    - Web-Common-Http
    state: present

- name: Install NET-Framework-Core from file
  ansible.windows.win_feature:
    name: NET-Framework-Core
    source: C:\Temp\iso\sources\sxs
    state: present

- name: Install IIS Web-Server with sub features and management tools
  ansible.windows.win_feature:
    name: Web-Server
    state: present
    include_sub_features: true
    include_management_tools: true
  register: win_feature

- name: Reboot if installing Web-Server feature requires it
  ansible.windows.win_reboot:
  when: win_feature.reboot_required
'''

RETURN = r'''
exitcode:
    description: The stringified exit code from the feature installation/removal command.
    returned: always
    type: str
    sample: Success
feature_result:
    description: List of features that were installed or removed.
    returned: success
    type: complex
    sample:
    contains:
        display_name:
            description: Feature display name.
            returned: always
            type: str
            sample: "Telnet Client"
        id:
            description: A list of KB article IDs that apply to the update.
            returned: always
            type: int
            sample: 44
        message:
            description: Any messages returned from the feature subsystem that occurred during installation or removal of this feature.
            returned: always
            type: list
            elements: str
            sample: []
        reboot_required:
            description: True when the target server requires a reboot as a result of installing or removing this feature.
            returned: always
            type: bool
            sample: true
        restart_needed:
            description: DEPRECATED in Ansible 2.4 (refer to C(reboot_required) instead). True when the target server requires a reboot as a
                         result of installing or removing this feature.
            returned: always
            type: bool
            sample: true
        skip_reason:
            description: The reason a feature installation or removal was skipped.
            returned: always
            type: str
            sample: NotSkipped
        success:
            description: If the feature installation or removal was successful.
            returned: always
            type: bool
            sample: true
reboot_required:
    description:
    - True when the target server indicates a reboot is required (no further updates can be installed until after a reboot).
    - This my be true even if not change had occurred as the value is derived from the server state.
    returned: success
    type: bool
    sample: true
'''
