# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: node_info
short_description: Information module for Node
description:
- Get all Node.
- Get Node by id.
- Get Node by name.
- This API allows the client to get all the node details.
- This API allows the client to get node details by ID.
- This API allows the client to get node details by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  name:
    description:
    - Name path parameter.
    type: str
  id:
    description:
    - Id path parameter.
    type: str
  page:
    description:
    - Page query parameter. Page number.
    type: int
  size:
    description:
    - Size query parameter. Number of objects returned per page.
    type: int
  filter:
    description:
    - >
      Filter query parameter. **Simple filtering** should be available through the filter query string parameter.
      The structure of a filter is a triplet of field operator and value separated with dots. More than one filter
      can be sent. The logical operator common to ALL filter criteria will be by default AND, and can be changed
      by using the "filterType=or" query string parameter.
    - Each resource Data model description should specify if an attribute is a filtered field.
    - The 'EQ' operator describes 'Equals'.
    - The 'NEQ' operator describes 'Not Equals'.
    - The 'GT' operator describes 'Greater Than'.
    - The 'LT' operator describes 'Less Than'.
    - The 'STARTSW' operator describes 'Starts With'.
    - The 'NSTARTSW' operator describes 'Not Starts With'.
    - The 'ENDSW' operator describes 'Ends With'.
    - The 'NENDSW' operator describes 'Not Ends With'.
    - The 'CONTAINS' operator describes 'Contains'.
    - The 'NCONTAINS' operator describes 'Not Contains'.
    elements: str
    type: list
  filterType:
    description:
    - >
      FilterType query parameter. The logical operator common to ALL filter criteria will be by default AND, and
      can be changed by using the parameter.
    type: str
requirements:
- ciscoisesdk >= 2.0.8
- python >= 3.5
seealso:
- name: Cisco ISE documentation for NodeDetails
  description: Complete reference of the NodeDetails API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!node
notes:
  - SDK Method used are
    node_details.NodeDetails.get_node_detail_by_id,
    node_details.NodeDetails.get_node_detail_by_name,
    node_details.NodeDetails.get_node_details_generator,

  - Paths used are
    get /ers/config/node,
    get /ers/config/node/name/{name},
    get /ers/config/node/{id},

"""

EXAMPLES = r"""
- name: Get all Node
  cisco.ise.node_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    page: 1
    size: 20
    filter: []
    filterType: AND
  register: result

- name: Get Node by id
  cisco.ise.node_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    id: string
  register: result

- name: Get Node by name
  cisco.ise.node_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    name: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "gateWay": "string",
      "userName": "string",
      "passWord": "string",
      "displayName": "string",
      "inDeployment": true,
      "otherPapFqdn": "string",
      "ipAddresses": [
        "string"
      ],
      "ipAddress": "string",
      "sxpIpAddress": "string",
      "nodeServiceTypes": "string",
      "fqdn": "string",
      "papNode": true,
      "primaryPapNode": true,
      "pxGridNode": true,
      "link": {
        "rel": "string",
        "href": "string",
        "type": "string"
      }
    }

ise_responses:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  version_added: '1.1.0'
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "gateWay": "string",
        "userName": "string",
        "passWord": "string",
        "displayName": "string",
        "inDeployment": true,
        "otherPapFqdn": "string",
        "ipAddresses": [
          "string"
        ],
        "ipAddress": "string",
        "sxpIpAddress": "string",
        "nodeServiceTypes": "string",
        "fqdn": "string",
        "papNode": true,
        "primaryPapNode": true,
        "pxGridNode": true,
        "link": {
          "rel": "string",
          "href": "string",
          "type": "string"
        }
      }
    ]
"""