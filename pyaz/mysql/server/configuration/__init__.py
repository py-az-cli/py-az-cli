from .... pyaz_utils import _call_az

def set(name, resource_group, server_name, value=None):
    '''
    Update the configuration of a server.
    '''
    return _call_az("az mysql server configuration set", locals())


def show(name, resource_group, server_name):
    '''
    Get the configuration for a server."
    '''
    return _call_az("az mysql server configuration show", locals())


def list(resource_group, server_name):
    '''
    List the configuration values for a server.
    '''
    return _call_az("az mysql server configuration list", locals())

