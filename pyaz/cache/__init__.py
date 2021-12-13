from .. pyaz_utils import call_az

def list(**kwargs):
    '''
    List the contents of the object cache.
    '''
    return call_az("az cache list", locals())


def show(name, resource_group, resource_type, **kwargs):
    '''
    Show the contents of a specific object in the cache.
    '''
    return call_az("az cache show", locals())


def delete(name, resource_group, resource_type, **kwargs):
    '''
    Delete an object from the cache.
    '''
    return call_az("az cache delete", locals())


def purge(**kwargs):
    '''
    Clear the entire CLI object cache.
    '''
    return call_az("az cache purge", locals())

