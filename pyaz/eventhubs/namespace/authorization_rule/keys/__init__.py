from ..... pyaz_utils import _call_az

def list(name, namespace_name, resource_group):
    '''
    Shows the connection strings for namespace
    '''
    return _call_az("az eventhubs namespace authorization-rule keys list", locals())


def renew(key, name, namespace_name, resource_group, key_value=None):
    '''
    Regenerate the connection strings of Authorizationrule for the namespace.
    '''
    return _call_az("az eventhubs namespace authorization-rule keys renew", locals())

