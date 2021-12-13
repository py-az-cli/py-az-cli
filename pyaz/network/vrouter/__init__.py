from ... pyaz_utils import call_az
from . import peering


def create(name, resource_group, hosted_gateway=None, hosted_subnet=None, location=None, tags=None, **kwargs):
    '''
    Create a virtual router.
    '''
    return call_az("az network vrouter create", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update a virtual router.
    '''
    return call_az("az network vrouter update", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete a virtual router under a resource group.
    '''
    return call_az("az network vrouter delete", locals())


def show(name, resource_group, **kwargs):
    '''
    Show a virtual router.
    '''
    return call_az("az network vrouter show", locals())


def list(resource_group=None, **kwargs):
    '''
    List all virtual routers under a subscription or a resource group.
    '''
    return call_az("az network vrouter list", locals())

