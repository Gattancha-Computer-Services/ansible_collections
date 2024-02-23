# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.plugin_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
    dnac_compare_equality,
    get_dict_result,
)
from ansible_collections.cisco.dnac.plugins.plugin_utils.exceptions import (
    InconsistentParameters,
)

# Get common arguments specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    state=dict(type="str", default="present", choices=["present", "absent"]),
    tags=dict(type="list"),
    deliveries=dict(type="list"),
    name=dict(type="str"),
    schedule=dict(type="dict"),
    view=dict(type="dict"),
    viewGroupId=dict(type="str"),
    viewGroupVersion=dict(type="str"),
    reportId=dict(type="str"),
))

required_if = [
    ("state", "present", ["name", "reportId"], True),
    ("state", "absent", ["name", "reportId"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class Reports(object):
    def __init__(self, params, dnac):
        self.dnac = dnac
        self.new_object = dict(
            tags=params.get("tags"),
            deliveries=params.get("deliveries"),
            name=params.get("name"),
            schedule=params.get("schedule"),
            view=params.get("view"),
            viewGroupId=params.get("viewGroupId"),
            viewGroupVersion=params.get("viewGroupVersion"),
            report_id=params.get("reportId"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        new_object_params['view_group_id'] = self.new_object.get('viewGroupId') or \
            self.new_object.get('view_group_id')
        new_object_params['view_id'] = self.new_object.get('view', {}).get('viewId')
        return new_object_params

    def create_params(self):
        new_object_params = {}
        new_object_params['tags'] = self.dnac.verify_array((self.new_object.get('tags')))
        new_object_params['deliveries'] = self.dnac.verify_array(self.new_object.get('deliveries'))
        new_object_params['name'] = self.new_object.get('name')
        new_object_params['schedule'] = self.new_object.get('schedule')
        new_object_params['view'] = self.new_object.get('view')
        new_object_params['viewGroupId'] = self.new_object.get('viewGroupId')
        new_object_params['viewGroupVersion'] = self.new_object.get('viewGroupVersion')
        return new_object_params

    def delete_by_id_params(self):
        new_object_params = {}
        new_object_params['report_id'] = self.new_object.get('report_id')
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method, using get all
        try:
            items = self.dnac.exec(
                family="reports",
                function="get_list_of_scheduled_reports",
                params=self.get_all_params(name=name),
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = get_dict_result(items, 'name', name)
        except Exception:
            result = None
        return result

    def get_object_by_id(self, id):
        result = None
        try:
            items = self.dnac.exec(
                family="reports",
                function="get_a_scheduled_report",
                params={"report_id": id}
            )
            if isinstance(items, dict):
                if 'response' in items:
                    items = items.get('response')
            result = get_dict_result(items, 'reportId', id)
        except Exception:
            result = None
        return result

    def exists(self):
        prev_obj = None
        id_exists = False
        name_exists = False
        o_id = self.new_object.get("id")
        o_id = o_id or self.new_object.get("report_id")
        name = self.new_object.get("name")
        if o_id:
            prev_obj = self.get_object_by_id(o_id)
            id_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if not id_exists and name:
            prev_obj = self.get_object_by_name(name)
            name_exists = prev_obj is not None and isinstance(prev_obj, dict)
        if name_exists:
            _id = prev_obj.get("id")
            _id = _id or prev_obj.get("reportId")
            if id_exists and name_exists and o_id != _id:
                raise InconsistentParameters("The 'id' and 'name' params don't refer to the same object")
            if _id:
                self.new_object.update(dict(id=_id))
                self.new_object.update(dict(report_id=_id))
            if _id:
                prev_obj = self.get_object_by_id(_id)
        it_exists = prev_obj is not None and isinstance(prev_obj, dict)
        return (it_exists, prev_obj)

    def requires_update(self, current_obj):
        requested_obj = self.new_object

        obj_params = [
            ("tags", "tags"),
            ("deliveries", "deliveries"),
            ("name", "name"),
            ("schedule", "schedule"),
            ("view", "view"),
            ("viewGroupId", "viewGroupId"),
            ("viewGroupVersion", "viewGroupVersion"),
            ("reportId", "report_id"),
        ]
        # Method 1. Params present in request (Ansible) obj are the same as the current (ISE) params
        # If any does not have eq params, it requires update
        return any(not dnac_compare_equality(current_obj.get(dnac_param),
                                             requested_obj.get(ansible_param))
                   for (dnac_param, ansible_param) in obj_params)

    def create(self):
        result = self.dnac.exec(
            family="reports",
            function="create_or_schedule_a_report",
            params=self.create_params(),
            op_modifies=True,
        )
        return result

    def delete(self):
        id = self.new_object.get("id")
        id = id or self.new_object.get("report_id")
        name = self.new_object.get("name")
        result = None
        if not id:
            prev_obj_name = self.get_object_by_name(name)
            id_ = None
            if prev_obj_name:
                id_ = prev_obj_name.get("id")
                id_ = id_ or prev_obj_name.get("reportId")
            if id_:
                self.new_object.update(dict(report_id=id_))
        result = self.dnac.exec(
            family="reports",
            function="delete_a_scheduled_report",
            params=self.delete_by_id_params(),
        )
        return result


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(self._task.args)
        obj = Reports(self._task.args, dnac)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = prev_obj
                    dnac.object_present_and_different()
                else:
                    response = prev_obj
                    dnac.object_already_present()
            else:
                response = obj.create()
                dnac.object_created()
        elif state == "absent":
            (obj_exists, prev_obj) = obj.exists()
            if obj_exists:
                response = obj.delete()
                dnac.object_deleted()
            else:
                dnac.object_already_absent()

        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
