from .... pyaz_utils import call_az

def add(hostname, name, resource_group, slot=None, **kwargs):
    '''
    Bind a hostname to a function app.
    '''
    return call_az("az functionapp config hostname add", locals())


def list(resource_group, webapp_name, slot=None, **kwargs):
    '''
    List all hostname bindings for a function app.
    '''
    return call_az("az functionapp config hostname list", locals())


def delete(hostname, name, resource_group, slot=None, **kwargs):
    '''
    Unbind a hostname from a function app.
    '''
    return call_az("az functionapp config hostname delete", locals())


def get_external_ip(name, resource_group, **kwargs):
    '''
    Get the external-facing IP address for a function app.
    '''
    return call_az("az functionapp config hostname get-external-ip", locals())

