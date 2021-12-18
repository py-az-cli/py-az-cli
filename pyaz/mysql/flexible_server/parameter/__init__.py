from .... pyaz_utils import _call_az

def set(name, resource_group, server_name, source=None, value=None):
    '''
    Update the parameter of a flexible server.
    '''
    return _call_az("az mysql flexible-server parameter set", locals())


def show(name, resource_group, server_name):
    '''
    Get the parameter for a flexible server."
    '''
    return _call_az("az mysql flexible-server parameter show", locals())


def list(resource_group, server_name):
    '''
    List the parameter values for a flexible server.
    '''
    return _call_az("az mysql flexible-server parameter list", locals())

