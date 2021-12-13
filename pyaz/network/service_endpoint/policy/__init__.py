from .... pyaz_utils import call_az

def create(name, resource_group, location=None, tags=None, **kwargs):
    '''
    Create a service endpoint policy.
    '''
    return call_az("az network service-endpoint policy create", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete a service endpoint policy.
    '''
    return call_az("az network service-endpoint policy delete", locals())


def list(resource_group=None, **kwargs):
    '''
    List service endpoint policies.
    '''
    return call_az("az network service-endpoint policy list", locals())


def show(name, resource_group, **kwargs):
    '''
    Get the details of a service endpoint policy.
    '''
    return call_az("az network service-endpoint policy show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update a service endpoint policy.
    '''
    return call_az("az network service-endpoint policy update", locals())

