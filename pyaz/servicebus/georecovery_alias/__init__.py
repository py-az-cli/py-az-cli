from ... pyaz_utils import call_az
from . import authorization_rule


def set(alias, namespace_name, partner_namespace, resource_group, alternate_name=None, **kwargs):
    '''
    Sets Service Bus Geo-Disaster Recovery Configuration Alias for the give Namespace
    '''
    return call_az("az servicebus georecovery-alias set", locals())


def show(alias, namespace_name, resource_group, **kwargs):
    '''
    shows properties of Service Bus Geo-Disaster Recovery Configuration Alias for Primay/Secondary Namespace
    '''
    return call_az("az servicebus georecovery-alias show", locals())


def list(namespace_name, resource_group, **kwargs):
    return call_az("az servicebus georecovery-alias list", locals())


def break_pair(alias, namespace_name, resource_group, **kwargs):
    '''
    Disables Service Bus Geo-Disaster Recovery Configuration Alias and stops replicating changes from primary to secondary namespaces
    '''
    return call_az("az servicebus georecovery-alias break-pair", locals())


def fail_over(alias, namespace_name, resource_group, parameters=None, **kwargs):
    '''
    Invokes Service Bus Geo-Disaster Recovery Configuration Alias failover and re-configure the alias to point to the secondary namespace
    '''
    return call_az("az servicebus georecovery-alias fail-over", locals())


def exists(alias, namespace_name, resource_group, **kwargs):
    '''
    Check if Geo Recovery Alias Name is available
    '''
    return call_az("az servicebus georecovery-alias exists", locals())


def delete(alias, namespace_name, resource_group, **kwargs):
    '''
    Deletes Service Bus Geo-Disaster Recovery Configuration Alias request accepted
    '''
    return call_az("az servicebus georecovery-alias delete", locals())

