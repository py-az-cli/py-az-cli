from ... pyaz_utils import call_az
from . import credential


def create(name, registry, expiration=None, expiration_in_days=None, gateway=None, no_passwords=None, repository=None, resource_group=None, scope_map=None, status=None, **kwargs):
    '''
    Create a token associated with a scope map for an Azure Container Registry.
    '''
    return call_az("az acr token create", locals())


def delete(name, registry, resource_group=None, yes=None, **kwargs):
    '''
    Delete a token for an Azure Container Registry.
    '''
    return call_az("az acr token delete", locals())


def update(name, registry, resource_group=None, scope_map=None, status=None, **kwargs):
    '''
    Update a token (replace associated scope map) for an Azure Container Registry.
    '''
    return call_az("az acr token update", locals())


def show(name, registry, resource_group=None, **kwargs):
    '''
    Show details and attributes of a token for an Azure Container Registry.
    '''
    return call_az("az acr token show", locals())


def list(registry, resource_group=None, **kwargs):
    '''
    List all tokens for an Azure Container Registry.
    '''
    return call_az("az acr token list", locals())

