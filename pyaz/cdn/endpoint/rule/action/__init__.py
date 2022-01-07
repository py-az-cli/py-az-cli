'''
Manage delivery rule actions for an endpoint.
'''
from ..... pyaz_utils import _call_az

def show(name, profile_name, resource_group):
    '''
    show delivery rules asscociate with the endpoint.

    Required Parameters:
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cdn endpoint rule action show", locals())


def add(action_name, name, profile_name, resource_group, rule_name, cache_behavior=None, cache_duration=None, custom_fragment=None, custom_hostname=None, custom_path=None, custom_querystring=None, destination=None, header_action=None, header_name=None, header_value=None, origin_group=None, preserve_unmatched_path=None, query_parameters=None, query_string_behavior=None, redirect_protocol=None, redirect_type=None, source_pattern=None):
    '''
    Add an action to a delivery rule.

    Required Parameters:
    - action_name -- Name of the action.
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.

    Optional Parameters:
    - cache_behavior -- Caching behavior for the requests.
    - cache_duration -- The duration for which the content needs to be cached.                Allowed format is [d.]hh:mm:ss.
    - custom_fragment -- Fragment to add to the redirect URL.
    - custom_hostname -- Host to redirect.                Leave empty to use the incoming host as the destination host.
    - custom_path -- The full path to redirect. Path cannot be empty and must start with /.                Leave empty to use the incoming path as destination path.
    - custom_querystring -- The set of query strings to be placed in the redirect URL.                leave empty to preserve the incoming query string.
    - destination -- The destination path to be used in the rewrite.
    - header_action -- Header action for the requests.
    - header_name -- Name of the header to modify.
    - header_value -- Value of the header.
    - origin_group -- Name or ID of the OriginGroup that would override the default OriginGroup
    - preserve_unmatched_path -- If True, the remaining path after the source                pattern will be appended to the new destination path.
    - query_parameters -- Query parameters to include or exclude (comma separated).
    - query_string_behavior -- Query string behavior for the requests.
    - redirect_protocol -- Protocol to use for the redirect.
    - redirect_type -- The redirect type the rule will use when redirecting traffic.
    - source_pattern -- A request URI pattern that identifies the type of requests that may be rewritten.
    '''
    return _call_az("az cdn endpoint rule action add", locals())


def remove(index, name, profile_name, resource_group, rule_name):
    '''
    Remove an action from a delivery rule.

    Required Parameters:
    - index -- The index of the condition/action
    - name -- Name of the CDN endpoint.
    - profile_name -- Name of the CDN profile which is unique within the resource group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - rule_name -- Name of the rule.
    '''
    return _call_az("az cdn endpoint rule action remove", locals())

