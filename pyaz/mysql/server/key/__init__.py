from .... pyaz_utils import _call_az

def create(kid, name, resource_group):
    '''
    Create server key.
    '''
    return _call_az("az mysql server key create", locals())


def delete(kid, name, resource_group, yes=None):
    '''
    Delete server key.
    '''
    return _call_az("az mysql server key delete", locals())


def show(kid, name, resource_group):
    '''
    Show server key.
    '''
    return _call_az("az mysql server key show", locals())


def list(name, resource_group):
    return _call_az("az mysql server key list", locals())

