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

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: gcp_cloudfunctions_cloud_function
description:
- A Cloud Function that contains user computation executed in response to an event.
short_description: Creates a GCP CloudFunction
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
    - A user-defined name of the function. Function names must be unique globally
      and match pattern `projects/*/locations/*/functions/*`.
    required: true
    type: str
  description:
    description:
    - User-provided description of a function.
    required: false
    type: str
  entry_point:
    description:
    - The name of the function (as defined in source code) that will be executed.
    - Defaults to the resource name suffix, if not specified. For backward compatibility,
      if function with given name is not found, then the system will try to use function
      named "function". For Node.js this is name of a function exported by the module
      specified in source_location.
    required: false
    type: str
  runtime:
    description:
    - The runtime in which to run the function. Required when deploying a new function,
      optional when updating an existing function.
    required: false
    type: str
  timeout:
    description:
    - The function execution timeout. Execution is considered failed and can be terminated
      if the function is not completed at the end of the timeout period. Defaults
      to 60 seconds.
    required: false
    type: str
  available_memory_mb:
    description:
    - The amount of memory in MB available for a function.
    required: false
    type: int
  labels:
    description:
    - A set of key/value label pairs associated with this Cloud Function.
    required: false
    type: dict
  environment_variables:
    description:
    - Environment variables that shall be available during function execution.
    required: false
    type: dict
  source_archive_url:
    description:
    - The Google Cloud Storage URL, starting with gs://, pointing to the zip archive
      which contains the function.
    required: false
    type: str
  source_upload_url:
    description:
    - The Google Cloud Storage signed URL used for source uploading.
    required: false
    type: str
  source_repository:
    description:
    - The source repository where a function is hosted.
    required: false
    type: dict
    suboptions:
      url:
        description:
        - The URL pointing to the hosted repository where the function is defined
          .
        required: true
        type: str
  https_trigger:
    description:
    - An HTTPS endpoint type of source that can be triggered via URL.
    required: false
    type: dict
    suboptions: {}
  event_trigger:
    description:
    - An HTTPS endpoint type of source that can be triggered via URL.
    required: false
    type: dict
    suboptions:
      event_type:
        description:
        - 'The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change`
          and `providers/cloud.pubsub/eventTypes/topic.publish`.'
        required: true
        type: str
      resource:
        description:
        - The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket.`
          .
        required: true
        type: str
      service:
        description:
        - The hostname of the service that should be observed.
        required: false
        type: str
  location:
    description:
    - The location of this cloud function.
    required: true
    type: str
  trigger_http:
    description:
    - Use HTTP to trigger this function.
    required: false
    type: bool
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
"""

EXAMPLES = """
- name: create a cloud function
  google.cloud.gcp_cloudfunctions_cloud_function:
    name: test_object
    location: us-central1
    entry_point: helloGET
    source_archive_url: gs://ansible-cloudfunctions-bucket/function.zip
    trigger_http: 'true'
    project: test_project
    auth_kind: serviceaccount
    service_account_file: "/tmp/auth.pem"
    state: present
"""

RETURN = """
name:
  description:
  - A user-defined name of the function. Function names must be unique globally and
    match pattern `projects/*/locations/*/functions/*`.
  returned: success
  type: str
description:
  description:
  - User-provided description of a function.
  returned: success
  type: str
status:
  description:
  - Status of the function deployment.
  returned: success
  type: str
entryPoint:
  description:
  - The name of the function (as defined in source code) that will be executed.
  - Defaults to the resource name suffix, if not specified. For backward compatibility,
    if function with given name is not found, then the system will try to use function
    named "function". For Node.js this is name of a function exported by the module
    specified in source_location.
  returned: success
  type: str
runtime:
  description:
  - The runtime in which the function is going to run. If empty, defaults to Node.js
    6.
  returned: success
  type: str
timeout:
  description:
  - The function execution timeout. Execution is considered failed and can be terminated
    if the function is not completed at the end of the timeout period. Defaults to
    60 seconds.
  returned: success
  type: str
availableMemoryMb:
  description:
  - The amount of memory in MB available for a function.
  returned: success
  type: int
serviceAccountEmail:
  description:
  - The email of the service account for this function.
  returned: success
  type: str
updateTime:
  description:
  - The last update timestamp of a Cloud Function.
  returned: success
  type: str
versionId:
  description:
  - The version identifier of the Cloud Function. Each deployment attempt results
    in a new version of a function being created.
  returned: success
  type: str
labels:
  description:
  - A set of key/value label pairs associated with this Cloud Function.
  returned: success
  type: dict
environmentVariables:
  description:
  - Environment variables that shall be available during function execution.
  returned: success
  type: dict
sourceArchiveUrl:
  description:
  - The Google Cloud Storage URL, starting with gs://, pointing to the zip archive
    which contains the function.
  returned: success
  type: str
sourceUploadUrl:
  description:
  - The Google Cloud Storage signed URL used for source uploading.
  returned: success
  type: str
sourceRepository:
  description:
  - The source repository where a function is hosted.
  returned: success
  type: complex
  contains:
    url:
      description:
      - The URL pointing to the hosted repository where the function is defined .
      returned: success
      type: str
    deployedUrl:
      description:
      - The URL pointing to the hosted repository where the function were defined
        at the time of deployment.
      returned: success
      type: str
httpsTrigger:
  description:
  - An HTTPS endpoint type of source that can be triggered via URL.
  returned: success
  type: complex
  contains:
    url:
      description:
      - The deployed url for the function.
      returned: success
      type: str
eventTrigger:
  description:
  - An HTTPS endpoint type of source that can be triggered via URL.
  returned: success
  type: complex
  contains:
    eventType:
      description:
      - 'The type of event to observe. For example: `providers/cloud.storage/eventTypes/object.change`
        and `providers/cloud.pubsub/eventTypes/topic.publish`.'
      returned: success
      type: str
    resource:
      description:
      - The resource(s) from which to observe events, for example, `projects/_/buckets/myBucket.`
        .
      returned: success
      type: str
    service:
      description:
      - The hostname of the service that should be observed.
      returned: success
      type: str
location:
  description:
  - The location of this cloud function.
  returned: success
  type: str
trigger_http:
  description:
  - Use HTTP to trigger this function.
  returned: success
  type: bool
"""

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
            state=dict(default="present", choices=["present", "absent"], type="str"),
            name=dict(required=True, type="str"),
            description=dict(type="str"),
            entry_point=dict(type="str"),
            runtime=dict(type="str"),
            timeout=dict(type="str"),
            available_memory_mb=dict(type="int"),
            labels=dict(type="dict"),
            environment_variables=dict(type="dict"),
            source_archive_url=dict(type="str"),
            source_upload_url=dict(type="str"),
            source_repository=dict(
                type="dict", options=dict(url=dict(required=True, type="str"))
            ),
            https_trigger=dict(type="dict", options=dict()),
            event_trigger=dict(
                type="dict",
                options=dict(
                    event_type=dict(required=True, type="str"),
                    resource=dict(required=True, type="str"),
                    service=dict(type="str"),
                ),
            ),
            location=dict(required=True, type="str"),
            trigger_http=dict(type="bool"),
        )
    )

    if not module.params["scopes"]:
        module.params["scopes"] = ["https://www.googleapis.com/auth/cloud-platform"]

    state = module.params["state"]

    fetch = fetch_resource(module, self_link(module))
    changed = False

    # Need to set triggerHttps to {} if boolean true.
    if fetch and fetch.get("httpsTrigger") and module.params["trigger_http"]:
        module.params["https_trigger"] = fetch.get("httpsTrigger")
    elif module.params["trigger_http"]:
        module.params["https_trigger"] = {}

    if fetch:
        if state == "present":
            if is_different(module, fetch):
                update(module, self_link(module), fetch)
                fetch = fetch_resource(module, self_link(module))
                changed = True
        else:
            delete(module, self_link(module))
            fetch = {}
            changed = True
    else:
        if state == "present":
            fetch = create(module, collection(module))
            changed = True
        else:
            fetch = {}

    fetch.update({"changed": changed})

    module.exit_json(**fetch)


def create(module, link):
    auth = GcpSession(module, "cloudfunctions")
    return wait_for_operation(module, auth.post(link, resource_to_request(module)))


def update(module, link, fetch):
    auth = GcpSession(module, "cloudfunctions")
    params = {
        "updateMask": updateMask(
            resource_to_request(module), response_to_hash(module, fetch)
        )
    }
    request = resource_to_request(module)
    del request["name"]
    return wait_for_operation(module, auth.put(link, request, params=params))


def updateMask(request, response):
    update_mask = []
    if request.get("name") != response.get("name"):
        update_mask.append("name")
    if request.get("description") != response.get("description"):
        update_mask.append("description")
    if request.get("entryPoint") != response.get("entryPoint"):
        update_mask.append("entryPoint")
    if request.get("runtime") != response.get("runtime"):
        update_mask.append("runtime")
    if request.get("timeout") != response.get("timeout"):
        update_mask.append("timeout")
    if request.get("availableMemoryMb") != response.get("availableMemoryMb"):
        update_mask.append("availableMemoryMb")
    if request.get("labels") != response.get("labels"):
        update_mask.append("labels")
    if request.get("environmentVariables") != response.get("environmentVariables"):
        update_mask.append("environmentVariables")
    if request.get("sourceArchiveUrl") != response.get("sourceArchiveUrl"):
        update_mask.append("sourceArchiveUrl")
    if request.get("sourceUploadUrl") != response.get("sourceUploadUrl"):
        update_mask.append("sourceUploadUrl")
    if request.get("sourceRepository") != response.get("sourceRepository"):
        update_mask.append("sourceRepository")
    if request.get("httpsTrigger") != response.get("httpsTrigger"):
        update_mask.append("httpsTrigger")
    if request.get("eventTrigger") != response.get("eventTrigger"):
        update_mask.append("eventTrigger")
    if request.get("location") != response.get("location"):
        update_mask.append("location")
    if request.get("trigger_http") != response.get("trigger_http"):
        update_mask.append("trigger_http")
    return ",".join(update_mask)


def delete(module, link):
    auth = GcpSession(module, "cloudfunctions")
    return wait_for_operation(module, auth.delete(link))


def resource_to_request(module):
    request = {
        "name": name_pattern(module.params.get("name"), module),
        "description": module.params.get("description"),
        "entryPoint": module.params.get("entry_point"),
        "runtime": module.params.get("runtime"),
        "timeout": module.params.get("timeout"),
        "availableMemoryMb": module.params.get("available_memory_mb"),
        "labels": module.params.get("labels"),
        "environmentVariables": module.params.get("environment_variables"),
        "sourceArchiveUrl": module.params.get("source_archive_url"),
        "sourceUploadUrl": module.params.get("source_upload_url"),
        "sourceRepository": CloudFunctionSourcerepository(
            module.params.get("source_repository", {}), module
        ).to_request(),
        "httpsTrigger": CloudFunctionHttpstrigger(
            module.params.get("https_trigger", {}), module
        ).to_request(),
        "eventTrigger": CloudFunctionEventtrigger(
            module.params.get("event_trigger", {}), module
        ).to_request(),
    }
    request = encode_request(request, module)
    return request


def fetch_resource(module, link, allow_not_found=True):
    auth = GcpSession(module, "cloudfunctions")
    return return_if_object(module, auth.get(link), allow_not_found)


def self_link(module):
    return "https://cloudfunctions.googleapis.com/v1/projects/{project}/locations/{location}/functions/{name}".format(
        **module.params
    )


def collection(module):
    return "https://cloudfunctions.googleapis.com/v1/projects/{project}/locations/{location}/functions".format(
        **module.params
    )


def return_if_object(module, response, allow_not_found=False):
    # If not found, return nothing.
    if allow_not_found and response.status_code == 404:
        return None

    # If no content, return nothing.
    if response.status_code == 204:
        return None

    try:
        module.raise_for_status(response)
        result = response.json()
    except getattr(json.decoder, "JSONDecodeError", ValueError):
        module.fail_json(msg="Invalid JSON response with error: %s" % response.text)

    if navigate_hash(result, ["error", "errors"]):
        module.fail_json(msg=navigate_hash(result, ["error", "errors"]))

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
        "name": response.get("name"),
        "description": response.get("description"),
        "status": response.get("status"),
        "entryPoint": response.get("entryPoint"),
        "runtime": response.get("runtime"),
        "timeout": response.get("timeout"),
        "availableMemoryMb": response.get("availableMemoryMb"),
        "serviceAccountEmail": response.get("serviceAccountEmail"),
        "updateTime": response.get("updateTime"),
        "versionId": response.get("versionId"),
        "labels": response.get("labels"),
        "environmentVariables": response.get("environmentVariables"),
        "sourceArchiveUrl": response.get("sourceArchiveUrl"),
        "sourceUploadUrl": response.get("sourceUploadUrl"),
        "sourceRepository": CloudFunctionSourcerepository(
            response.get("sourceRepository", {}), module
        ).from_response(),
        "httpsTrigger": CloudFunctionHttpstrigger(
            response.get("httpsTrigger", {}), module
        ).from_response(),
        "eventTrigger": CloudFunctionEventtrigger(
            response.get("eventTrigger", {}), module
        ).from_response(),
    }


def name_pattern(name, module):
    if name is None:
        return

    regex = r"projects/.*/locations/.*/functions/.*"

    if not re.match(regex, name):
        name = "projects/{project}/locations/{location}/functions/{name}".format(
            **module.params
        )

    return name


def async_op_url(module, extra_data=None):
    if extra_data is None:
        extra_data = {}
    url = "https://cloudfunctions.googleapis.com/v1/{op_id}"
    combined = extra_data.copy()
    combined.update(module.params)
    return url.format(**combined)


def wait_for_operation(module, response):
    op_result = return_if_object(module, response)
    if op_result is None:
        return {}
    status = navigate_hash(op_result, ["done"])
    wait_done = wait_for_completion(status, op_result, module)
    raise_if_errors(wait_done, ["error"], module)
    return navigate_hash(wait_done, ["response"])


def wait_for_completion(status, op_result, module):
    op_id = navigate_hash(op_result, ["name"])
    op_uri = async_op_url(module, {"op_id": op_id})
    while not status:
        raise_if_errors(op_result, ["error"], module)
        time.sleep(1.0)
        op_result = fetch_resource(module, op_uri, False)
        status = navigate_hash(op_result, ["done"])
    return op_result


def raise_if_errors(response, err_path, module):
    errors = navigate_hash(response, err_path)
    if errors is not None:
        module.fail_json(msg=errors)


def encode_request(request, module):
    return_vals = {}
    for k, v in request.items():
        if v or v is False:
            return_vals[k] = v

    if module.params["trigger_http"] and not return_vals.get("httpsTrigger"):
        return_vals["httpsTrigger"] = {}

    return return_vals


class CloudFunctionSourcerepository(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({"url": self.request.get("url")})

    def from_response(self):
        return remove_nones_from_dict({"url": self.request.get("url")})


class CloudFunctionHttpstrigger(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict({})

    def from_response(self):
        return remove_nones_from_dict({})


class CloudFunctionEventtrigger(object):
    def __init__(self, request, module):
        self.module = module
        if request:
            self.request = request
        else:
            self.request = {}

    def to_request(self):
        return remove_nones_from_dict(
            {
                "eventType": self.request.get("event_type"),
                "resource": self.request.get("resource"),
                "service": self.request.get("service"),
            }
        )

    def from_response(self):
        return remove_nones_from_dict(
            {
                "eventType": self.request.get("eventType"),
                "resource": self.request.get("resource"),
                "service": self.request.get("service"),
            }
        )


if __name__ == "__main__":
    main()
