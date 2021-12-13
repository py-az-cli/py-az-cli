from ... pyaz_utils import call_az

def list(location=None, resource_group=None, **kwargs):
    '''
    List security alerts.
    '''
    return call_az("az security alert list", locals())


def show(location, name, resource_group=None, **kwargs):
    '''
    Shows a security alert.
    '''
    return call_az("az security alert show", locals())


def update(location, name, status, resource_group=None, **kwargs):
    '''
    Updates a security alert status.
    '''
    return call_az("az security alert update", locals())

