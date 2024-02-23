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
module: gcp_compute_firewall_info
description:
- Gather info for GCP Firewall
short_description: Gather info for GCP Firewall
author: Google Inc. (@googlecloudplatform)
requirements:
- python >= 2.6
- requests >= 2.18.4
- google-auth >= 1.3.0
options:
  filters:
    description:
    - A list of filter value pairs. Available filters are listed here U(https://cloud.google.com/sdk/gcloud/reference/topic/filters).
    - Each additional filter in the list will act be added as an AND condition (filter1
      and filter2) .
    type: list
    elements: str
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
- name: get info on a firewall
  gcp_compute_firewall_info:
    filters:
    - name = test_object
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
    allowed:
      description:
      - The list of ALLOW rules specified by this firewall. Each rule specifies a
        protocol and port-range tuple that describes a permitted connection.
      returned: success
      type: complex
      contains:
        ip_protocol:
          description:
          - The IP protocol to which this rule applies. The protocol type is required
            when creating a firewall rule. This value can either be one of the following
            well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all),
            or the IP protocol number.
          returned: success
          type: str
        ports:
          description:
          - An optional list of ports to which this rule applies. This field is only
            applicable for UDP or TCP protocol. Each entry must be either an integer
            or a range. If not specified, this rule applies to connections through
            any port.
          - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
          returned: success
          type: list
    creationTimestamp:
      description:
      - Creation timestamp in RFC3339 text format.
      returned: success
      type: str
    denied:
      description:
      - The list of DENY rules specified by this firewall. Each rule specifies a protocol
        and port-range tuple that describes a denied connection.
      returned: success
      type: complex
      contains:
        ip_protocol:
          description:
          - The IP protocol to which this rule applies. The protocol type is required
            when creating a firewall rule. This value can either be one of the following
            well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all),
            or the IP protocol number.
          returned: success
          type: str
        ports:
          description:
          - An optional list of ports to which this rule applies. This field is only
            applicable for UDP or TCP protocol. Each entry must be either an integer
            or a range. If not specified, this rule applies to connections through
            any port.
          - 'Example inputs include: ["22"], ["80","443"], and ["12345-12349"].'
          returned: success
          type: list
    description:
      description:
      - An optional description of this resource. Provide this property when you create
        the resource.
      returned: success
      type: str
    destinationRanges:
      description:
      - If destination ranges are specified, the firewall will apply only to traffic
        that has destination IP address in these ranges. These ranges must be expressed
        in CIDR format. Only IPv4 is supported.
      returned: success
      type: list
    direction:
      description:
      - 'Direction of traffic to which this firewall applies; default is INGRESS.
        Note: For INGRESS traffic, it is NOT supported to specify destinationRanges;
        For EGRESS traffic, it is NOT supported to specify sourceRanges OR sourceTags.'
      returned: success
      type: str
    disabled:
      description:
      - Denotes whether the firewall rule is disabled, i.e not applied to the network
        it is associated with. When set to true, the firewall rule is not enforced
        and the network behaves as if it did not exist. If this is unspecified, the
        firewall rule will be enabled.
      returned: success
      type: bool
    logConfig:
      description:
      - This field denotes the logging options for a particular firewall rule.
      - If logging is enabled, logs will be exported to Cloud Logging.
      returned: success
      type: complex
      contains:
        enable:
          description:
          - This field denotes whether to enable logging for a particular firewall
            rule. If logging is enabled, logs will be exported to Stackdriver.
          returned: success
          type: bool
        metadata:
          description:
          - This field denotes whether to include or exclude metadata for firewall
            logs.
          returned: success
          type: str
    id:
      description:
      - The unique identifier for the resource.
      returned: success
      type: int
    name:
      description:
      - Name of the resource. Provided by the client when the resource is created.
        The name must be 1-63 characters long, and comply with RFC1035. Specifically,
        the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?`
        which means the first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last character,
        which cannot be a dash.
      returned: success
      type: str
    network:
      description:
      - 'URL of the network resource for this firewall rule. If not specified when
        creating a firewall rule, the default network is used: global/networks/default
        If you choose to specify this property, you can specify the network as a full
        or partial URL. For example, the following are all valid URLs: U(https://www.googleapis.com/compute/v1/projects/myproject/global/)
        networks/my-network projects/myproject/global/networks/my-network global/networks/default
        .'
      returned: success
      type: dict
    priority:
      description:
      - Priority for this rule. This is an integer between 0 and 65535, both inclusive.
        When not specified, the value assumed is 1000. Relative priorities determine
        precedence of conflicting rules. Lower value of priority implies higher precedence
        (eg, a rule with priority 0 has higher precedence than a rule with priority
        1). DENY rules take precedence over ALLOW rules having equal priority.
      returned: success
      type: int
    sourceRanges:
      description:
      - If source ranges are specified, the firewall will apply only to traffic that
        has source IP address in these ranges. These ranges must be expressed in CIDR
        format. One or both of sourceRanges and sourceTags may be set. If both properties
        are set, the firewall will apply to traffic that has source IP address within
        sourceRanges OR the source IP that belongs to a tag listed in the sourceTags
        property. The connection does not need to match both properties for the firewall
        to apply. Only IPv4 is supported.
      returned: success
      type: list
    sourceServiceAccounts:
      description:
      - If source service accounts are specified, the firewall will apply only to
        traffic originating from an instance with a service account in this list.
        Source service accounts cannot be used to control traffic to an instance's
        external IP address because service accounts are associated with an instance,
        not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts.
        If both are set, the firewall will apply to traffic that has source IP address
        within sourceRanges OR the source IP belongs to an instance with service account
        listed in sourceServiceAccount. The connection does not need to match both
        properties for the firewall to apply. sourceServiceAccounts cannot be used
        at the same time as sourceTags or targetTags.
      returned: success
      type: list
    sourceTags:
      description:
      - If source tags are specified, the firewall will apply only to traffic with
        source IP that belongs to a tag listed in source tags. Source tags cannot
        be used to control traffic to an instance's external IP address. Because tags
        are associated with an instance, not an IP address. One or both of sourceRanges
        and sourceTags may be set. If both properties are set, the firewall will apply
        to traffic that has source IP address within sourceRanges OR the source IP
        that belongs to a tag listed in the sourceTags property. The connection does
        not need to match both properties for the firewall to apply.
      returned: success
      type: list
    targetServiceAccounts:
      description:
      - A list of service accounts indicating sets of instances located in the network
        that may make network connections as specified in allowed[].
      - targetServiceAccounts cannot be used at the same time as targetTags or sourceTags.
        If neither targetServiceAccounts nor targetTags are specified, the firewall
        rule applies to all instances on the specified network.
      returned: success
      type: list
    targetTags:
      description:
      - A list of instance tags indicating sets of instances located in the network
        that may make network connections as specified in allowed[].
      - If no targetTags are specified, the firewall rule applies to all instances
        on the specified network.
      returned: success
      type: list
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
    module = GcpModule(argument_spec=dict(filters=dict(type='list', elements='str')))

    if not module.params['scopes']:
        module.params['scopes'] = ['https://www.googleapis.com/auth/compute']

    return_value = {'resources': fetch_list(module, collection(module), query_options(module.params['filters']))}
    module.exit_json(**return_value)


def collection(module):
    return "https://compute.googleapis.com/compute/v1/projects/{project}/global/firewalls".format(**module.params)


def fetch_list(module, link, query):
    auth = GcpSession(module, 'compute')
    return auth.list(link, return_if_object, array_name='items', params={'filter': query})


def query_options(filters):
    if not filters:
        return ''

    if len(filters) == 1:
        return filters[0]
    else:
        queries = []
        for f in filters:
            # For multiple queries, all queries should have ()
            if f[0] != '(' and f[-1] != ')':
                queries.append("(%s)" % ''.join(f))
            else:
                queries.append(f)

        return ' '.join(queries)


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
