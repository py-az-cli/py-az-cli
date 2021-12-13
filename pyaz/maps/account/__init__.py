from ... pyaz_utils import call_az
from . import keys


def show(name, resource_group, **kwargs):
    '''
    Show the details of a maps account.
    '''
    return call_az("az maps account show", locals())


def list(resource_group=None, **kwargs):
    '''
    Show all maps accounts in a subscription or in a resource group.
    '''
    return call_az("az maps account list", locals())


def create(name, resource_group, sku, accept_tos=None, disable_local_auth=None, kind=None, linked_resources=None, tags=None, type=None, user_identities=None, **kwargs):
    '''
    Create a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs.
    '''
    return call_az("az maps account create", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete a Maps Account.
    '''
    return call_az("az maps account delete", locals())


def update(name, resource_group, sku, disable_local_auth=None, kind=None, linked_resources=None, tags=None, type=None, user_identities=None, **kwargs):
    '''
    Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku, Tags, Properties.
    '''
    return call_az("az maps account update", locals())

