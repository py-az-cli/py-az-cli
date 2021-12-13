from .. pyaz_utils import call_az

def create(lock_type, name, namespace=None, notes=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Create a lock.
    '''
    return call_az("az lock create", locals())


def delete(ids=None, name=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Delete a lock.
    '''
    return call_az("az lock delete", locals())


def list(filter_string=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    List lock information.
    '''
    return call_az("az lock list", locals())


def show(ids=None, name=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Show the properties of a lock
    '''
    return call_az("az lock show", locals())


def update(ids=None, lock_type=None, name=None, namespace=None, notes=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Update a lock.
    '''
    return call_az("az lock update", locals())

