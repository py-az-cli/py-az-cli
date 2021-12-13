from .... pyaz_utils import call_az

def set(name, resource_group, server_name, value=None, **kwargs):
    '''
    Update the configuration of a server.
    '''
    return call_az("az mariadb server configuration set", locals())


def show(name, resource_group, server_name, **kwargs):
    '''
    Get the configuration for a server."
    '''
    return call_az("az mariadb server configuration show", locals())


def list(resource_group, server_name, **kwargs):
    '''
    List the configuration values for a server.
    '''
    return call_az("az mariadb server configuration list", locals())

