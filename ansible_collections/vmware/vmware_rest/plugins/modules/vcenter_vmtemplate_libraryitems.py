# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vmtemplate_libraryitems
short_description: Creates a library item in content library from a virtual machine
description: Creates a library item in content library from a virtual machine. This
    {@term operation} creates a library item in content library whose content is a
    virtual machine template created from the source virtual machine, using the supplied
    create specification. The virtual machine template is stored in a newly created
    library item.
options:
    description:
        description:
        - Description of the deployed virtual machine.
        type: str
    disk_storage:
        description:
        - Storage specification for the virtual machine template's disks.
        - 'Valid attributes are:'
        - ' - C(datastore) (str): Identifier for the datastore associated the deployed
            virtual machine''s disk. ([''deploy'', ''present''])'
        - ' - C(storage_policy) (dict): Storage policy for the deployed virtual machine''s
            disk. ([''deploy'', ''present''])'
        - '   - Accepted keys:'
        - '     - type (string): Policy type for a virtual machine template''s disk.'
        - 'Accepted value for this field:'
        - '       - C(USE_SPECIFIED_POLICY)'
        - '     - policy (string): Identifier for the storage policy to use.'
        type: dict
    disk_storage_overrides:
        description:
        - Storage specification for individual disks in the deployed virtual machine.
            This is specified as a mapping between disk identifiers in the source
            virtual machine template contained in the library item and their storage
            specifications.
        type: dict
    guest_customization:
        description:
        - Guest customization spec to apply to the deployed virtual machine.
        - 'Valid attributes are:'
        - ' - C(name) (str): Name of the customization specification. ([''deploy''])'
        type: dict
    hardware_customization:
        description:
        - Hardware customization spec which specifies updates to the deployed virtual
            machine.
        - 'Valid attributes are:'
        - ' - C(nics) (dict): Map of Ethernet network adapters to update. ([''deploy''])'
        - ' - C(disks_to_remove) (list): Idenfiers of disks to remove from the deployed
            virtual machine. ([''deploy''])'
        - ' - C(disks_to_update) (dict): Disk update specification for individual
            disks in the deployed virtual machine. ([''deploy''])'
        - ' - C(cpu_update) (dict): CPU update specification for the deployed virtual
            machine. ([''deploy''])'
        - '   - Accepted keys:'
        - '     - num_cpus (integer): Number of virtual processors in the deployed
            virtual machine.'
        - '     - num_cores_per_socket (integer): Number of cores among which to distribute
            CPUs in the deployed virtual machine.'
        - ' - C(memory_update) (dict): Memory update specification for the deployed
            virtual machine. ([''deploy''])'
        - '   - Accepted keys:'
        - '     - memory (integer): Size of a virtual machine''s memory in MB.'
        type: dict
    library:
        description:
        - Identifier of the library in which the new library item should be created.
            Required with I(state=['present'])
        type: str
    name:
        description:
        - Name of the deployed virtual machine. This parameter is mandatory.
        required: true
        type: str
    placement:
        description:
        - Information used to place the virtual machine template.
        - 'Valid attributes are:'
        - ' - C(folder) (str): Virtual machine folder into which the deployed virtual
            machine should be placed. ([''deploy'', ''present''])'
        - ' - C(resource_pool) (str): Resource pool into which the deployed virtual
            machine should be placed. ([''deploy'', ''present''])'
        - ' - C(host) (str): Host onto which the virtual machine should be placed.
            If C(#host) and C(#resource_pool) are both specified, C(#resource_pool)
            must belong to C(#host). If C(#host) and C(#cluster) are both specified,
            C(#host) must be a member of C(#cluster). ([''deploy'', ''present''])'
        - ' - C(cluster) (str): Cluster onto which the deployed virtual machine should
            be placed. If C(#cluster) and C(#resource_pool) are both specified, C(#resource_pool)
            must belong to C(#cluster). If C(#cluster) and C(#host) are both specified,
            C(#host) must be a member of C(#cluster). ([''deploy'', ''present''])'
        type: dict
    powered_on:
        description:
        - Specifies whether the deployed virtual machine should be powered on after
            deployment.
        type: bool
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    source_vm:
        description:
        - Identifier of the source virtual machine to create the library item from.
            Required with I(state=['present'])
        type: str
    state:
        choices:
        - deploy
        - present
        default: present
        description: []
        type: str
    template_library_item:
        description:
        - identifier of the content library item containing the source virtual machine
            template to be deployed. Required with I(state=['deploy'])
        type: str
    vcenter_hostname:
        description:
        - The hostname or IP address of the vSphere vCenter
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_HOST) will be used instead.
        required: true
        type: str
    vcenter_password:
        description:
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
        type: str
    vcenter_username:
        description:
        - The vSphere vCenter username
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_USER) will be used instead.
        required: true
        type: str
    vcenter_validate_certs:
        default: true
        description:
        - Allows connection when SSL certificates are not valid. Set to C(false) when
            certificates are not trusted.
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_VALIDATE_CERTS) will be used instead.
        type: bool
    vm_home_storage:
        description:
        - Storage location for the virtual machine template's configuration and log
            files.
        - 'Valid attributes are:'
        - ' - C(datastore) (str): Identifier of the datastore for the deployed virtual
            machine''s configuration and log files. ([''deploy'', ''present''])'
        - ' - C(storage_policy) (dict): Storage policy for the deployed virtual machine''s
            configuration and log files. ([''deploy'', ''present''])'
        - '   - Accepted keys:'
        - '     - type (string): Policy type for the virtual machine template''s configuration
            and log files.'
        - 'Accepted value for this field:'
        - '       - C(USE_SPECIFIED_POLICY)'
        - '     - policy (string): Identifier for the storage policy to use.'
        type: dict
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.2.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      datastore: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    name: test_vm1
    guest_OS: RHEL_7_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
    disks:
    - type: SATA
      backing:
        type: VMDK_FILE
        vmdk_file: '[local] test_vm1/{{ disk_name }}.vmdk'
    - type: SATA
      new_vmdk:
        name: second_disk
        capacity: 32000000000
    cdroms:
    - type: SATA
      sata:
        bus: 0
        unit: 2
    nics:
    - backing:
        type: STANDARD_PORTGROUP
        network: "{{ lookup('vmware.vmware_rest.network_moid', '/my_dc/network/VM Network') }}"
  register: my_vm

- name: Create a content library based on a DataStore
  vmware.vmware_rest.content_locallibrary:
    name: my_library_on_datastore
    description: automated
    publish_info:
      published: true
      authentication_method: NONE
    storage_backings:
    - datastore_id: "{{ lookup('vmware.vmware_rest.datastore_moid', '/my_dc/datastore/local') }}"
      type: DATASTORE
    state: present
  register: nfs_lib

- name: Create a VM template on the library
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: golden-template
    library: '{{ nfs_lib.id }}'
    source_vm: '{{ my_vm.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
  register: mylib_item

- name: Get the list of items of the NFS library
  vmware.vmware_rest.content_library_item_info:
    library_id: '{{ nfs_lib.id }}'
  register: lib_items

- name: Use the name to identify the item
  set_fact:
    my_template_item: "{{ lib_items.value | selectattr('name', 'equalto', 'golden-template')|first }}"

- name: Deploy a new VM based on the template
  vmware.vmware_rest.vcenter_vmtemplate_libraryitems:
    name: vm-from-template
    library: '{{ nfs_lib.id }}'
    template_library_item: '{{ my_template_item.id }}'
    placement:
      cluster: "{{ lookup('vmware.vmware_rest.cluster_moid', '/my_dc/host/my_cluster') }}"
      folder: "{{ lookup('vmware.vmware_rest.folder_moid', '/my_dc/vm') }}"
      resource_pool: "{{ lookup('vmware.vmware_rest.resource_pool_moid', '/my_dc/host/my_cluster/Resources') }}"
    state: deploy
  register: my_new_vm
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Create a VM template on the library
id:
  description: moid of the resource
  returned: On success
  sample: 9c6df1f5-faba-490c-a8e6-edb72f787ab8
  type: str
value:
  description: Create a VM template on the library
  returned: On success
  sample:
    cpu:
      cores_per_socket: 1
      count: 1
    disks:
      '16000':
        capacity: 16106127360
        disk_storage:
          datastore: datastore-1122
      '16001':
        capacity: 32000000000
        disk_storage:
          datastore: datastore-1122
    guest_OS: RHEL_7_64
    memory:
      size_MiB: 1024
    nics:
      '4000':
        backing_type: STANDARD_PORTGROUP
        mac_type: ASSIGNED
        network: network-1123
    vm_home_storage:
      datastore: datastore-1122
    vm_template: vm-1132
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "create": {
        "query": {},
        "body": {
            "description": "description",
            "disk_storage": "disk_storage",
            "disk_storage_overrides": "disk_storage_overrides",
            "library": "library",
            "name": "name",
            "placement": "placement",
            "source_vm": "source_vm",
            "vm_home_storage": "vm_home_storage",
        },
        "path": {},
    },
    "deploy": {
        "query": {},
        "body": {
            "description": "description",
            "disk_storage": "disk_storage",
            "disk_storage_overrides": "disk_storage_overrides",
            "guest_customization": "guest_customization",
            "hardware_customization": "hardware_customization",
            "name": "name",
            "placement": "placement",
            "powered_on": "powered_on",
            "vm_home_storage": "vm_home_storage",
        },
        "path": {"template_library_item": "template_library_item"},
    },
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["description"] = {"type": "str"}
    argument_spec["disk_storage"] = {"type": "dict"}
    argument_spec["disk_storage_overrides"] = {"type": "dict"}
    argument_spec["guest_customization"] = {"type": "dict"}
    argument_spec["hardware_customization"] = {"type": "dict"}
    argument_spec["library"] = {"type": "str"}
    argument_spec["name"] = {"required": True, "type": "str"}
    argument_spec["placement"] = {"type": "dict"}
    argument_spec["powered_on"] = {"type": "bool"}
    argument_spec["source_vm"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["deploy", "present"],
        "default": "present",
    }
    argument_spec["template_library_item"] = {"type": "str"}
    argument_spec["vm_home_storage"] = {"type": "dict"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return (
        "https://{vcenter_hostname}" "/api/vcenter/vm-template/library-items"
    ).format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):

    lookup_url = "https://{vcenter_hostname}/api/content/library/item?library_id={library}".format(
        **params
    )
    per_id_url = "https://{vcenter_hostname}/api/content/library/item".format(**params)
    uniquity_keys = ["name"]
    comp_func = None

    _json = None

    if params["template_library_item"]:
        _json = await get_device_info(
            session, build_url(params), params["template_library_item"]
        )

    if not _json and (uniquity_keys or comp_func):
        _json = await exists(
            params,
            session,
            url=lookup_url,
            uniquity_keys=uniquity_keys,
            per_id_url=per_id_url,
            comp_func=comp_func,
        )

    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["template_library_item"] = _json["id"]
            return await globals()["_update"](params, session)

        extra_info_url = "https://{vcenter_hostname}/api/vcenter/vm-template/library-items/{id}".format(
            **params, id=_json["id"]
        )
        async with session.get(extra_info_url) as resp:
            if resp.status == 200:
                extra_json = await resp.json()
                for k, v in extra_json.items():
                    _json["value"][k] = v

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm-template/library-items"
    ).format(**params)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _deploy(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["deploy"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["deploy"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/vm-template/library-items/{template_library_item}?action=deploy"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm-template/library-items/{template_library_item}?action=deploy"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "deploy")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
