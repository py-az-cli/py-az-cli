from ... pyaz_utils import call_az

def create(lock_type, name, notes=None, resource_group=None, **kwargs):
    '''
    Create a subscription lock.
    '''
    return call_az("az account lock create", locals())


def delete(ids=None, name=None, resource_group=None, **kwargs):
    '''
    Delete a subscription lock.
    '''
    return call_az("az account lock delete", locals())


def list(filter_string=None, resource_group=None, **kwargs):
    '''
    List lock information in the subscription.
    '''
    return call_az("az account lock list", locals())


def show(ids=None, name=None, resource_group=None, **kwargs):
    '''
    Show the details of a subscription lock
    '''
    return call_az("az account lock show", locals())


def update(ids=None, lock_type=None, name=None, notes=None, resource_group=None, **kwargs):
    '''
    Update a subscription lock.
    '''
    return call_az("az account lock update", locals())

