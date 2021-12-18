from ... pyaz_utils import _call_az

def assign(name, resource_group, identities=None, role=None, scope=None):
    '''
    assign managed identity to the static web app
    '''
    return _call_az("az staticwebapp identity assign", locals())


def remove(name, resource_group, identities=None, yes=None):
    '''
    Disable static web app's managed identity
    '''
    return _call_az("az staticwebapp identity remove", locals())


def show(name, resource_group):
    '''
    display static web app's managed identity
    '''
    return _call_az("az staticwebapp identity show", locals())

