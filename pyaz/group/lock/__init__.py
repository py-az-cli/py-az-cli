from ... pyaz_utils import call_az

def create(lock_type, name, resource_group, notes=None, **kwargs):
    '''
    Create a resource group lock.
    '''
    return call_az("az group lock create", locals())


def delete(ids=None, name=None, resource_group=None, **kwargs):
    '''
    Delete a resource group lock.
    '''
    return call_az("az group lock delete", locals())


def list(filter_string=None, resource_group=None, **kwargs):
    '''
    List lock information in the resource-group.
    '''
    return call_az("az group lock list", locals())


def show(ids=None, name=None, resource_group=None, **kwargs):
    '''
    Show the details of a resource group lock
    '''
    return call_az("az group lock show", locals())


def update(ids=None, lock_type=None, name=None, notes=None, resource_group=None, **kwargs):
    '''
    Update a resource group lock.
    '''
    return call_az("az group lock update", locals())

