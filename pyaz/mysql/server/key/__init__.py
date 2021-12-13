from .... pyaz_utils import call_az

def create(kid, name, resource_group, **kwargs):
    '''
    Create server key.
    '''
    return call_az("az mysql server key create", locals())


def delete(kid, name, resource_group, yes=None, **kwargs):
    '''
    Delete server key.
    '''
    return call_az("az mysql server key delete", locals())


def show(kid, name, resource_group, **kwargs):
    '''
    Show server key.
    '''
    return call_az("az mysql server key show", locals())


def list(name, resource_group, **kwargs):
    return call_az("az mysql server key list", locals())

