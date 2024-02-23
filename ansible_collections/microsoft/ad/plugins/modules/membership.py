# -*- coding: utf-8 -*-

# Copyright (c) 2022 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
module: membership
short_description: Manage domain/workgroup membership for a Windows host
description:
- Manages domain membership or workgroup membership for a Windows host. Also supports hostname changes.
- This module may require subsequent use of the M(ansible.windows.win_reboot) action if changes are made.
options:
  dns_domain_name:
    description:
    - When I(state=domain), this is the DNS name of the domain to which the targeted Windows host should be joined.
    - This cannot be set when I(offline_join_blob) is specified.
    type: str
  domain_admin_user:
    description:
    - Username of a domain admin for the target domain (required to join or leave the domain).
    - This must be set unless I(offline_join_blob) is specified.
    type: str
  domain_admin_password:
    description:
    - Password for the specified C(domain_admin_user).
    - This must be set unless I(offline_join_blob) is specified.
    type: str
  domain_ou_path:
    description:
    - The desired OU path for adding the computer object.
    - This is only used when adding the target host to a domain, if it is already a member then it is ignored.
    - This cannot be set when I(offline_join_blob) is specified.
    type: str
  hostname:
    description:
    - The desired hostname for the Windows host.
    - This cannot be set when I(offline_join_blob) is specified.
    type: str
  offline_join_blob:
    description:
    - The base64 string of the domain offline join blob to use when joining
      the host to a domain.
    - This blob can been generated by the
      M(microsoft.ad.offline_join) module.
    - This is mutually exclusive with I(domain_admin_user), I(dns_domain_name),
      and I(domain_ou_path).
    - It also cannot be used with I(hostname).
    type: str
  reboot:
    description:
    - If C(true), this will reboot the host if a reboot was required to configure the domain.
    - If C(false), this will not reboot the host if a reboot was required and instead sets the I(reboot_required) return value to C(true).
    - If changing from a domain to workgroup, the connection account must be a local user that can connect to the host
      after it has unjoined the domain.
    - This cannot be used with async mode.
    - To use this parameter, ensure the fully qualified module name is used in the task or the I(collections) keyword includes this collection.
    type: bool
    default: false
  state:
    description:
    - Whether the target host should be a member of a domain or workgroup.
    - When I(state=domain), I(dns_domain_name), I(domain_admin_user), and I(domain_admin_password) or
      I(offline_join_blob) must be set.
    - When I(state=workgroup), I(workgroup_name) must be set.
    choices:
    - domain
    - workgroup
    required: true
    type: str
  workgroup_name:
    description:
    - When I(state=workgroup), this is the name of the workgroup that the Windows host should be in.
    type: str
extends_documentation_fragment:
- ansible.builtin.action_common_attributes
- ansible.builtin.action_common_attributes.flow
attributes:
  check_mode:
    support: full
  diff_mode:
    support: full
  platform:
    platforms:
    - windows
  action:
    support: full
  async:
    support: partial
    details: Supported for all scenarios except with I(reboot=True).
  bypass_host_loop:
    support: none
seealso:
- module: microsoft.ad.domain
- module: microsoft.ad.domain_controller
- module: microsoft.ad.group
- module: microsoft.ad.offline_join
- module: microsoft.ad.user
- module: microsoft.ad.computer
- module: ansible.windows.win_group
- module: ansible.windows.win_group_membership
- module: ansible.windows.win_user
- ref: Migration guide <ansible_collections.microsoft.ad.docsite.guide_migration.migrated_modules.win_domain_membership>
  description: This module replaces C(ansible.windows.win_domain_membership). See the migration guide for details.
- module: ansible.windows.win_domain_membership
author:
- Matt Davis (@nitzmahone)
- Jordan Borean (@jborean93)
"""

EXAMPLES = r"""
- name: join host to ansible.vagrant with automatic reboot
  microsoft.ad.membership:
    dns_domain_name: ansible.vagrant
    hostname: mydomainclient
    domain_admin_user: testguy@ansible.vagrant
    domain_admin_password: password123!
    domain_ou_path: "OU=Windows,OU=Servers,DC=ansible,DC=vagrant"
    state: domain
    reboot: true

- name: join host to workgroup with manual reboot in later task
  microsoft.ad.membership:
    workgroup_name: mywg
    domain_admin_user: '{{ win_domain_admin_user }}'
    domain_admin_password: '{{ win_domain_admin_password }}'
    state: workgroup
  register: workgroup_res

- name: reboot host after joining workgroup
  ansible.windows.win_reboot:
  when: workgroup_res.reboot_required
"""

RETURN = r"""
reboot_required:
  description: True if changes were made that require a reboot.
  returned: always
  type: bool
  sample: true
"""