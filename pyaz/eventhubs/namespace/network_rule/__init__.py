from .... pyaz_utils import _call_az

def add(namespace_name, resource_group, action=None, ignore_missing_endpoint=None, ip_address=None, subnet=None, vnet_name=None):
    '''
    Add a network rule for a namespace.
    '''
    return _call_az("az eventhubs namespace network-rule add", locals())


def list(namespace_name, resource_group):
    '''
    Show properties of Network rule of the given Namespace.
    '''
    return _call_az("az eventhubs namespace network-rule list", locals())


def remove(namespace_name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Remove network rule for a namespace
    '''
    return _call_az("az eventhubs namespace network-rule remove", locals())

