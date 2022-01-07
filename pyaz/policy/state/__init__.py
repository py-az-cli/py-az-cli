'''
Manage policy compliance states.
'''
from ... pyaz_utils import _call_az

def list(all=None, apply=None, expand=None, filter=None, from_=None, management_group=None, namespace=None, order_by=None, parent=None, policy_assignment=None, policy_definition=None, policy_set_definition=None, resource=None, resource_group=None, resource_type=None, select=None, to=None, top=None):
    '''
    List policy compliance states.

    Optional Parameters:
    - all -- Within the specified time interval, get all policy states instead of the latest only.
    - apply -- Apply expression for aggregations using OData notation.
    - expand -- Expand expression using OData notation.
    - filter -- Filter expression using OData notation.
    - from_ -- ISO 8601 formatted timestamp specifying the start time of the interval to query.
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - order_by -- Ordering expression using OData notation.
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - policy_assignment -- Name of policy assignment.
    - policy_definition -- Name of policy definition.
    - policy_set_definition -- Name of policy set definition.
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    - select -- Select expression using OData notation.
    - to -- ISO 8601 formatted timestamp specifying the end time of the interval to query.
    - top -- Maximum number of records to return.
    '''
    return _call_az("az policy state list", locals())


def summarize(filter=None, from_=None, management_group=None, namespace=None, parent=None, policy_assignment=None, policy_definition=None, policy_set_definition=None, resource=None, resource_group=None, resource_type=None, to=None, top=None):
    '''
    Summarize policy compliance states.

    Optional Parameters:
    - filter -- Filter expression using OData notation.
    - from_ -- ISO 8601 formatted timestamp specifying the start time of the interval to query.
    - management_group -- Name of management group.
    - namespace -- Provider namespace (Ex: Microsoft.Provider).
    - parent -- The parent path (Ex: resourceTypeA/nameA/resourceTypeB/nameB).
    - policy_assignment -- Name of policy assignment.
    - policy_definition -- Name of policy definition.
    - policy_set_definition -- Name of policy set definition.
    - resource -- Resource ID or resource name. If a name is given, please provide the resource group and other relevant resource id arguments.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - resource_type -- Resource type (Ex: resourceTypeC).
    - to -- ISO 8601 formatted timestamp specifying the end time of the interval to query.
    - top -- Maximum number of records to return.
    '''
    return _call_az("az policy state summarize", locals())


def trigger_scan(no_wait=None, resource_group=None):
    '''
    Trigger a policy compliance evaluation for a scope.

    Optional Parameters:
    - no_wait -- Do not wait for the long-running operation to finish.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az policy state trigger-scan", locals())

