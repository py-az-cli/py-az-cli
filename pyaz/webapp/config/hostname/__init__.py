from .... pyaz_utils import call_az

def add(hostname, resource_group, webapp_name, slot=None, **kwargs):
    '''
    Bind a hostname to a web app.
    '''
    return call_az("az webapp config hostname add", locals())


def list(resource_group, webapp_name, slot=None, **kwargs):
    '''
    List all hostname bindings for a web app.
    '''
    return call_az("az webapp config hostname list", locals())


def delete(hostname, resource_group, webapp_name, slot=None, **kwargs):
    '''
    Unbind a hostname from a web app.
    '''
    return call_az("az webapp config hostname delete", locals())


def get_external_ip(resource_group, webapp_name, **kwargs):
    '''
    Get the external-facing IP address for a web app.
    '''
    return call_az("az webapp config hostname get-external-ip", locals())

