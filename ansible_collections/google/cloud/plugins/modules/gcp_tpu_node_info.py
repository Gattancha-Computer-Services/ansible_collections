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
module: gcp_tpu_node_info
description:
- Gather info for GCP Node
short_description: Gather info for GCP Node
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  zone:
    description:
    - The GCP location for the TPU. If it is not provided, the provider zone is used.
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
- name: get info on a node
  gcp_tpu_node_info:
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
      - The immutable name of the TPU.
      returned: success
      type: str
    description:
      description:
      - The user-supplied description of the TPU. Maximum of 512 characters.
      returned: success
      type: str
    acceleratorType:
      description:
      - The type of hardware accelerators associated with this node.
      returned: success
      type: str
    tensorflowVersion:
      description:
      - The version of Tensorflow running in the Node.
      returned: success
      type: str
    network:
      description:
      - The name of a network to peer the TPU node to. It must be a preexisting Compute
        Engine network inside of the project on which this API has been activated.
        If none is provided, "default" will be used.
      returned: success
      type: str
    cidrBlock:
      description:
      - The CIDR block that the TPU node will use when selecting an IP address. This
        CIDR block must be a /29 block; the Compute Engine networks API forbids a
        smaller block, and using a larger block would be wasteful (a node can only
        consume one IP address).
      - Errors will occur if the CIDR block has already been used for a currently
        existing TPU node, the CIDR block conflicts with any subnetworks in the user's
        provided network, or the provided network is peered with another network that
        is using that CIDR block.
      returned: success
      type: str
    serviceAccount:
      description:
      - The service account used to run the tensor flow services within the node.
        To share resources, including Google Cloud Storage data, with the Tensorflow
        job running in the Node, this account must have permissions to that data.
      returned: success
      type: str
    useServiceNetworking:
      description:
      - Whether the VPC peering for the node is set up through Service Networking
        API.
      - The VPC Peering should be set up before provisioning the node. If this field
        is set, cidr_block field should not be specified. If the network that you
        want to peer the TPU Node to is a Shared VPC network, the node must be created
        with this this field enabled.
      returned: success
      type: bool
    schedulingConfig:
      description:
      - Sets the scheduling options for this TPU instance.
      returned: success
      type: complex
      contains:
        preemptible:
          description:
          - Defines whether the TPU instance is preemptible.
          returned: success
          type: bool
    networkEndpoints:
      description:
      - The network endpoints where TPU workers can be accessed and sent work.
      - It is recommended that Tensorflow clients of the node first reach out to the
        first (index 0) entry.
      returned: success
      type: complex
      contains:
        ipAddress:
          description:
          - The IP address of this network endpoint.
          returned: success
          type: str
        port:
          description:
          - The port of this network endpoint.
          returned: success
          type: int
    labels:
      description:
      - Resource labels to represent user provided metadata.
      returned: success
      type: dict
    zone:
      description:
      - The GCP location for the TPU. If it is not provided, the provider zone is
        used.
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
    module = GcpModule(argument_spec=dict(zone=dict(type='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/cloud-platform']

    return_value = {'resources': fetch_list(module, collection(module))}
    module.exit_json(**return_value)


def collection(module):
    return "https://tpu.googleapis.com/v1/projects/{project}/locations/{zone}/nodes".format(**module.params)


def fetch_list(module, link):
    auth = GcpSession(module, 'tpu')
    return auth.list(link, return_if_object, array_name='nodes')


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
