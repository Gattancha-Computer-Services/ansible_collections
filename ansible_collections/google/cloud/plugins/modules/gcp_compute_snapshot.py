# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Google
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# ----------------------------------------------------------------------------
#
#     ***     AUTO GENERATED CODE    ***    Type: MMv1     ***
#
# ----------------------------------------------------------------------------
#
#     This file is automatically generated by Magic Modules and manual
#     changes will be clobbered when the file is regenerated.
#
#     Please read more about how to change this file at
#     https://www.github.com/GoogleCloudPlatform/magic-modules
#
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function

__metaclass__ = type

################################################################################
# Documentation
################################################################################

ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ["preview"], 'supported_by': 'community'}

DOCUMENTATION = '''
---
module: gcp_compute_snapshot
description:
- Represents a Persistent Disk Snapshot resource.
- Use snapshots to back up data from your persistent disks. Snapshots are different
  from public images and custom images, which are used primarily to create instances
  or configure instance templates. Snapshots are useful for periodic backup of the
  data on your persistent disks. You can create snapshots from persistent disks even
  while they are attached to running instances.
- Snapshots are incremental, so you can create regular snapshots on a persistent disk
  faster and at a much lower cost than if you regularly created a full image of the
  disk.
short_description: Creates a GCP Snapshot
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  state:
    description:
    - Whether the given object should exist in GCP
    choices:
    - present
    - absent
    default: present
    type: str
  name:
    description:
    - Name of the resource; provided by the client when the resource is created. The
      name must be 1-63 characters long, and comply with RFC1035. Specifically, the
      name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
      which means the first character must be a lowercase letter, and all following
      characters must be a dash, lowercase letter, or digit, except the last character,
      which cannot be a dash.
    required: true
    type: str
  description:
    description:
    - An optional description of this resource.
    required: false
    type: str
  storage_locations:
    description:
    - Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
    elements: str
    required: false
    type: list
  labels:
    description:
    - Labels to apply to this Snapshot.
    required: false
    type: dict
  source_disk:
    description:
    - A reference to the disk used to create this snapshot.
    - 'This field represents a link to a Disk resource in GCP. It can be specified
      in two ways. First, you can place a dictionary with key ''name'' and value of
      your resource''s name Alternatively, you can add `register: name-of-resource`
      to a gcp_compute_disk task and then set this source_disk field to "{{ name-of-resource
      }}"'
    required: true
    type: dict
  zone:
    description:
    - A reference to the zone where the disk is hosted.
    required: false
    type: str
  snapshot_encryption_key:
    description:
    - The customer-supplied encryption key of the snapshot. Required if the source
      snapshot is protected by a customer-supplied encryption key.
    required: false
    type: dict
    suboptions:
      raw_key:
        description:
        - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
          base64 to either encrypt or decrypt this resource.
        required: false
        type: str
      kms_key_name:
        description:
        - The name of the encryption key that is stored in Google Cloud KMS.
        required: false
        type: str
      kms_key_service_account:
        description:
        - The service account used for the encryption request for the given KMS key.
        - If absent, the Compute Engine Service Agent service account is used.
        required: false
        type: str
  source_disk_encryption_key:
    description:
    - The customer-supplied encryption key of the source snapshot. Required if the
      source snapshot is protected by a customer-supplied encryption key.
    required: false
    type: dict
    suboptions:
      raw_key:
        description:
        - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
          base64 to either encrypt or decrypt this resource.
        required: false
        type: str
      kms_key_name:
        description:
        - The name of the encryption key that is stored in Google Cloud KMS.
        required: false
        type: str
      kms_key_service_account:
        description:
        - The service account used for the encryption request for the given KMS key.
        - If absent, the Compute Engine Service Agent service account is used.
        required: false
        type: str
  project:
    description:
    - The Google Cloud Platform project to use.
    type: str
  auth_kind:
    description:
    - The type of credential used.
    type: str
    required: true
    choices:
    - application
    - machineaccount
    - serviceaccount
  service_account_contents:
    description:
    - The contents of a Service Account JSON file, either in a dictionary or as a
      JSON string that represents it.
    type: jsonarg
  service_account_file:
    description:
    - The path of a Service Account JSON file if serviceaccount is selected as type.
    type: path
  service_account_email:
    description:
    - An optional service account email address if machineaccount is selected and
      the user does not wish to use the default email.
    type: str
  scopes:
    description:
    - Array of scopes to be used
    type: list
    elements: str
  env_type:
    description:
    - Specifies which Ansible environment you're running this module within.
    - This should not be set unless you know what you're doing.
    - This only alters the User Agent string for any API requests.
    type: str
notes:
- 'API Reference: U(https://cloud.google.com/compute/docs/reference/rest/v1/snapshots)'
- 'Official Documentation: U(https://cloud.google.com/compute/docs/disks/create-snapshots)'
- for authentication, you can set service_account_file using the C(GCP_SERVICE_ACCOUNT_FILE)
  env variable.
- for authentication, you can set service_account_contents using the C(GCP_SERVICE_ACCOUNT_CONTENTS)
  env variable.
- For authentication, you can set service_account_email using the C(GCP_SERVICE_ACCOUNT_EMAIL)
  env variable.
- For authentication, you can set auth_kind using the C(GCP_AUTH_KIND) env variable.
- For authentication, you can set scopes using the C(GCP_SCOPES) env variable.
- Environment variables values will only be used if the playbook values are not set.
- The I(service_account_email) and I(service_account_file) options are mutually exclusive.
'''

EXAMPLES = '''
- name: create a disk
  google.cloud.gcp_compute_disk:
    name: disk-snapshot
    zone: us-central1-a
    project: "{{ gcp_project }}"
    auth_kind: "{{ gcp_cred_kind }}"
    service_account_file: "{{ gcp_cred_file }}"
    state: present
  register: disk

- name: create a snapshot
  google.cloud.gcp_compute_snapshot:
    name: test_object
    source_disk: "{{ disk }}"
    zone: us-central1-a
    labels:
      my_label: value
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
'''

RETURN = '''
creationTimestamp:
  description:
  - Creation timestamp in RFC3339 text format.
  returned: success
  type: str
id:
  description:
  - The unique identifier for the resource.
  returned: success
  type: int
diskSizeGb:
  description:
  - Size of the snapshot, specified in GB.
  returned: success
  type: int
name:
  description:
  - Name of the resource; provided by the client when the resource is created. The
    name must be 1-63 characters long, and comply with RFC1035. Specifically, the
    name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
    which means the first character must be a lowercase letter, and all following
    characters must be a dash, lowercase letter, or digit, except the last character,
    which cannot be a dash.
  returned: success
  type: str
description:
  description:
  - An optional description of this resource.
  returned: success
  type: str
storageBytes:
  description:
  - A size of the storage used by the snapshot. As snapshots share storage, this number
    is expected to change with snapshot creation/deletion.
  returned: success
  type: int
storageLocations:
  description:
  - Cloud Storage bucket storage location of the snapshot (regional or multi-regional).
  returned: success
  type: list
licenses:
  description:
  - A list of public visible licenses that apply to this snapshot. This can be because
    the original image had licenses attached (such as a Windows image). snapshotEncryptionKey
    nested object Encrypts the snapshot using a customer-supplied encryption key.
  returned: success
  type: list
labels:
  description:
  - Labels to apply to this Snapshot.
  returned: success
  type: dict
labelFingerprint:
  description:
  - The fingerprint used for optimistic locking of this resource. Used internally
    during updates.
  returned: success
  type: str
sourceDisk:
  description:
  - A reference to the disk used to create this snapshot.
  returned: success
  type: dict
zone:
  description:
  - A reference to the zone where the disk is hosted.
  returned: success
  type: str
snapshotEncryptionKey:
  description:
  - The customer-supplied encryption key of the snapshot. Required if the source snapshot
    is protected by a customer-supplied encryption key.
  returned: success
  type: complex
  contains:
    rawKey:
      description:
      - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
        base64 to either encrypt or decrypt this resource.
      returned: success
      type: str
    sha256:
      description:
      - The RFC 4648 base64 encoded SHA-256 hash of the customer-supplied encryption
        key that protects this resource.
      returned: success
      type: str
    kmsKeyName:
      description:
      - The name of the encryption key that is stored in Google Cloud KMS.
      returned: success
      type: str
    kmsKeyServiceAccount:
      description:
      - The service account used for the encryption request for the given KMS key.
      - If absent, the Compute Engine Service Agent service account is used.
      returned: success
      type: str
sourceDiskEncryptionKey:
  description:
  - The customer-supplied encryption key of the source snapshot. Required if the source
    snapshot is protected by a customer-supplied encryption key.
  returned: success
  type: complex
  contains:
    rawKey:
      description:
      - Specifies a 256-bit customer-supplied encryption key, encoded in RFC 4648
        base64 to either encrypt or decrypt this resource.
      returned: success
      type: str
    kmsKeyName:
      description:
      - The name of the encryption key that is stored in Google Cloud KMS.
      returned: success
      type: str
    kmsKeyServiceAccount:
      description:
      - The service account used for the encryption request for the given KMS key.
      - If absent, the Compute Engine Service Agent service account is used.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################

from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import (
    navigate_hash,
    GcpSession,
    GcpModule,
    GcpRequest,
    remove_nones_from_dict,
    replace_resource_dict,
)
import json
import re
import time

################################################################################
# Main
################################################################################


def main():
    """Main function"""

    module = GcpModule(
        argument_spec=dict(
            state=dict(default='present', choices=['present', 'absent'], type='str'),
            name=dict(required=True, type='str'),
            description=dict(type='str'),
            storage_locations=dict(type='list', elements='str'),
            labels=dict(type='dict'),
            source_disk=dict(required=True, type='dict'),
            zone=dict(type='str'),
            snapshot_encryption_key=dict(
                type='dict', no_log=True, options=dict(raw_key=dict(type='str'), kms_key_name=dict(type='str'), kms_key_service_account=dict(type='str'))
            ),
            source_disk_encryption_key=dict(
                type='dict', no_log=True, options=dict(raw_key=dict(type='str'), kms_key_name=dict(type='str'), kms_key_service_account=dict(type='str'))
            ),
        )
    )

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    state = module.params['state']
    kind = 'compute#snapshot'

    fetch = fetch_resource(module, self_link(module), kind)
    changed = False

    if fetch:
        if state == 'present':
            if is_different(module, fetch):
                update(module, self_link(module), kind, fetch)
                fetch = fetch_resource(module, self_link(module), kind)
                changed = True
        else:
            delete(module, self_link(module), kind)
            fetch = {}
            changed = True
    else:
        if state == 'present':
            fetch = create(module, create_link(module), kind)
            changed = True
        else:
            fetch = {}

    fetch.update({'changed': changed})

    module.exit_json(**fetch)


def create(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, kind, fetch):
    update_fields(module, resource_to_request(module), response_to_hash(module, fetch))
    return fetch_resource(module, self_link(module), kind)


def update_fields(module, request, response):
    if response.get('labels') != request.get('labels'):
        labels_update(module, request, response)


def labels_update(module, request, response):
    auth = GcpSession(module, 'compute')
    auth.post(
        ''.join(["https://compute.googleapis.com/compute/v1/", "projects/{project}/global/snapshots/{name}/setLabels"]).format(**module.params),
        {u'labels': module.params.get('labels'), u'labelFingerprint': response.get('labelFingerprint')},
    )


def delete(module, link, kind):
    auth = GcpSession(module, 'compute')
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        u'kind': 'compute#snapshot',
        u'sourceDisk': replace_resource_dict(module.params.get(u'source_disk', {}), 'name'),
        u'zone': module.params.get('zone'),
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'storageLocations': module.params.get('storage_locations'),
        u'labels': module.params.get('labels'),
    }
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    return return_vals


def fetch_resource(module, link, kind, allow_not_found=True):
    auth = GcpSession(module, 'compute')
    return return_if_object(module, auth.get(link), kind, allow_not_found)


def self_link(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/snapshots/{name}".format(**module.params)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/snapshots".format(**module.params)


def create_link(module):
    res = {'project': module.params['project'], 'zone': module.params['zone'], 'source_disk': replace_resource_dict(module.params['source_disk'], 'name')}
    return "https://compute.googleapis.com/compute/v1/projects/{project}/zones/{zone}/disks/{source_disk}/createSnapshot".format(**res)


def return_if_object(module, response, kind, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


def is_different(module, response):
    request = resource_to_request(module)
    response = response_to_hash(module, response)

    # Remove all output-only from response.
    response_vals = {}
    for k, v in response.items():
        if k in request:
            response_vals[k] = v

    request_vals = {}
    for k, v in request.items():
        if k in response:
            request_vals[k] = v

    return GcpRequest(request_vals) != GcpRequest(response_vals)


# Remove unnecessary properties from the response.
# This is for doing comparisons with Ansible's current parameters.
def response_to_hash(module, response):
    return {
        u'creationTimestamp': response.get(u'creationTimestamp'),
        u'id': response.get(u'id'),
        u'diskSizeGb': response.get(u'diskSizeGb'),
        u'name': module.params.get('name'),
        u'description': module.params.get('description'),
        u'storageBytes': response.get(u'storageBytes'),
        u'storageLocations': response.get(u'storageLocations'),
        u'licenses': response.get(u'licenses'),
        u'labels': response.get(u'labels'),
        u'labelFingerprint': response.get(u'labelFingerprint'),
    }


def license_selflink(name, params):
    if name is None:
        return
    url = r"https://compute.googleapis.com/compute/v1//projects/.*/global/licenses/.*"
    if not re.match(url, name):
        name = "https://compute.googleapis.com/compute/v1//projects/{project}/global/licenses/%s".format(**params) % name
    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://compute.googleapis.com/compute/v1/"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response, 'compute#operation')
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ['status'])
    wait_done = wait_for_completion(status, op_result, module)
    return fetch_resource(module, navigate_hash(wait_done, ['targetLink']), 'compute#snapshot')


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ['name'])
    op_uri = navigate_hash(op_result, ['selfLink'])
    while status != 'DONE':
        raise_if_errors(op_result, ['error', 'errors'], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, 'compute#operation', False)
        status = navigate_hash(op_result, ['status'])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


class SnapshotSnapshotencryptionkey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'rawKey': self.request.get('raw_key'),
                u'kmsKeyName': self.request.get('kms_key_name'),
                u'kmsKeyServiceAccount': self.request.get('kms_key_service_account'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'rawKey': self.request.get(u'rawKey'),
                u'kmsKeyName': self.request.get(u'kmsKeyName'),
                u'kmsKeyServiceAccount': self.request.get(u'kmsKeyServiceAccount'),
            }
        )


class SnapshotSourcediskencryptionkey(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                u'rawKey': self.request.get('raw_key'),
                u'kmsKeyName': self.request.get('kms_key_name'),
                u'kmsKeyServiceAccount': self.request.get('kms_key_service_account'),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                u'rawKey': self.request.get(u'rawKey'),
                u'kmsKeyName': self.request.get(u'kmsKeyName'),
                u'kmsKeyServiceAccount': self.request.get(u'kmsKeyServiceAccount'),
            }
        )


if __name__ == '__main__':
    main()