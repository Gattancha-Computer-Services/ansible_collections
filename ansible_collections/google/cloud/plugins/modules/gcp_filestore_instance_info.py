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
module: gcp_filestore_instance_info
description:
- Gather info for GCP Instance
short_description: Gather info for GCP Instance
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  zone:
    description:
    - The name of the Filestore zone of the instance.
    required: true
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
- name: get info on an instance
  gcp_filestore_instance_info:
    zone: us-central1-b
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
'''

RETURN = '''
resources:
  description: List of resources
  returned: always
  type: complex
  contains:
    name:
      description:
      - The resource name of the instance.
      returned: success
      type: str
    description:
      description:
      - A description of the instance.
      returned: success
      type: str
    createTime:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    tier:
      description:
      - The service tier of the instance.
      returned: success
      type: str
    labels:
      description:
      - Resource labels to represent user-provided metadata.
      returned: success
      type: dict
    fileShares:
      description:
      - File system shares on the instance. For this version, only a single file share
        is supported.
      returned: success
      type: complex
      contains:
        name:
          description:
          - The name of the fileshare (16 characters or less) .
          returned: success
          type: str
        capacityGb:
          description:
          - File share capacity in GiB. This must be at least 1024 GiB for the standard
            tier, or 2560 GiB for the premium tier.
          returned: success
          type: int
    networks:
      description:
      - VPC networks to which the instance is connected. For this version, only a
        single network is supported.
      returned: success
      type: complex
      contains:
        network:
          description:
          - The name of the GCE VPC network to which the instance is connected.
          returned: success
          type: str
        modes:
          description:
          - IP versions for which the instance has IP addresses assigned.
          returned: success
          type: list
        reservedIpRange:
          description:
          - A /29 CIDR block that identifies the range of IP addresses reserved for
            this instance.
          returned: success
          type: str
        ipAddresses:
          description:
          - A list of IPv4 or IPv6 addresses.
          returned: success
          type: list
    etag:
      description:
      - Server-specified ETag for the instance resource to prevent simultaneous updates
        from overwriting each other.
      returned: success
      type: str
    zone:
      description:
      - The name of the Filestore zone of the instance.
      returned: success
      type: str
'''

################################################################################
# Imports
################################################################################
from ansible_collections.google.cloud.plugins.module_utils.gcp_utils import navigate_hash, GcpSession, GcpModule, GcpRequest
import json

################################################################################
# Main
################################################################################


def main():
    module = GcpModule(argument_spec=dict(zone=dict(required=True, type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    return "https://file.googleapis.com/v1/projects/{project}/locations/{zone}/instances".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'filestore')
    return auth.list(link, return_if_object, array_name='instances')


def return_if_object(module, response):
    # If not found, return nothing.
    if response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, 'JSONDecodeError', ValueError) as inst:
        module.fail_json(msg="Invalid JSON response with error: %s" % inst)

    if navigate_hash(result, ['error', 'errors']):
        module.fail_json(msg=navigate_hash(result, ['error', 'errors']))

    return result


if __name__ == "__main__":
    main()
