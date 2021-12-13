from .... pyaz_utils import call_az

def create(kid, managed_instance, resource_group, **kwargs):
    '''
    Creates a SQL Instance key.
    '''
    return call_az("az sql mi key create", locals())


def delete(kid, managed_instance, resource_group, **kwargs):
    '''
    Deletes a SQL Instance key.
    '''
    return call_az("az sql mi key delete", locals())


def show(kid, managed_instance, resource_group, **kwargs):
    '''
    Shows a SQL Instance key.
    '''
    return call_az("az sql mi key show", locals())


def list(managed_instance, resource_group, filter=None, **kwargs):
    return call_az("az sql mi key list", locals())

