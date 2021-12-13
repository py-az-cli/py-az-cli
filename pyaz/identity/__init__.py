from .. pyaz_utils import call_az

def create(name, resource_group, location=None, tags=None, **kwargs):
    return call_az("az identity create", locals())


def show(name, resource_group, **kwargs):
    return call_az("az identity show", locals())


def delete(name, resource_group, **kwargs):
    return call_az("az identity delete", locals())


def list(resource_group=None, **kwargs):
    '''
    List Managed Service Identities
    '''
    return call_az("az identity list", locals())


def list_operations(**kwargs):
    '''
    Lists available operations for the Managed Identity provider
    '''
    return call_az("az identity list-operations", locals())

