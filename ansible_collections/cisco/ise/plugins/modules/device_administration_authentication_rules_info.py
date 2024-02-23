# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_administration_authentication_rules_info
short_description: Information module for Device Administration Authentication Rules
description:
- Get all Device Administration Authentication Rules.
- Get Device Administration Authentication Rules by id.
- Device Admin - Get authentication rules.
- Device Admin - Get rule attributes.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.ise.module_info
author: Rafael Campos (@racampos)
options:
  policyId:
    description:
    - PolicyId path parameter. Policy id.
    type: str
  id:
    description:
    - Id path parameter. Rule id.
    type: str
requirements:
- ciscoisesdk >= 2.0.8
- python >= 3.5
seealso:
- name: Cisco ISE documentation for Device Administration - Authentication Rules
  description: Complete reference of the Device Administration - Authentication Rules API.
  link: https://developer.cisco.com/docs/identity-services-engine/v1/#!policy-openapi
notes:
  - SDK Method used are
    device_administration_authentication_rules.DeviceAdministrationAuthenticationRules.get_device_admin_authentication_rule_by_id,
    device_administration_authentication_rules.DeviceAdministrationAuthenticationRules.get_device_admin_authentication_rules,

  - Paths used are
    get /device-admin/policy-set/{policyId}/authentication,
    get /device-admin/policy-set/{policyId}/authentication/{id},

"""

EXAMPLES = r"""
- name: Get all Device Administration Authentication Rules
  cisco.ise.device_administration_authentication_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
  register: result

- name: Get Device Administration Authentication Rules by id
  cisco.ise.device_administration_authentication_rules_info:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    policyId: string
    id: string
  register: result

"""

RETURN = r"""
ise_response:
  description: A dictionary or list with the response returned by the Cisco ISE Python SDK
  returned: always
  type: dict
  sample: >
    {
      "identitySourceName": "string",
      "ifAuthFail": "string",
      "ifProcessFail": "string",
      "ifUserNotFound": "string",
      "link": {
        "href": "string",
        "rel": "string",
        "type": "string"
      },
      "rule": {
        "condition": {
          "conditionType": "string",
          "isNegate": true,
          "link": {
            "href": "string",
            "rel": "string",
            "type": "string"
          },
          "description": "string",
          "id": "string",
          "name": "string",
          "attributeName": "string",
          "attributeValue": "string",
          "dictionaryName": "string",
          "dictionaryValue": "string",
          "operator": "string",
          "children": [
            {
              "conditionType": "string",
              "isNegate": true,
              "link": {
                "href": "string",
                "rel": "string",
                "type": "string"
              }
            }
          ],
          "datesRange": {
            "endDate": "string",
            "startDate": "string"
          },
          "datesRangeException": {
            "endDate": "string",
            "startDate": "string"
          },
          "hoursRange": {
            "endTime": "string",
            "startTime": "string"
          },
          "hoursRangeException": {
            "endTime": "string",
            "startTime": "string"
          },
          "weekDays": [
            "string"
          ],
          "weekDaysException": [
            "string"
          ]
        },
        "default": true,
        "hitCounts": 0,
        "id": "string",
        "name": "string",
        "rank": 0,
        "state": "string"
      }
    }
"""