from .. pyaz_utils import call_az
from . import lock, management_group


def list(all=None, refresh=None, **kwargs):
    '''
    Get a list of subscriptions for the logged in account. By default, only 'Enabled' subscriptions from the current cloud is shown.
    '''
    return call_az("az account list", locals())


def set(subscription, **kwargs):
    '''
    Set a subscription to be the current active subscription.
    '''
    return call_az("az account set", locals())


def show(sdk_auth=None, subscription=None, **kwargs):
    '''
    Get the details of a subscription.
    '''
    return call_az("az account show", locals())


def clear(**kwargs):
    '''
    Clear all subscriptions from the CLI's local cache.
    '''
    return call_az("az account clear", locals())


def list_locations(**kwargs):
    '''
    List supported regions for the current subscription.
    '''
    return call_az("az account list-locations", locals())


def get_access_token(resource=None, resource_type=None, scope=None, subscription=None, tenant=None, **kwargs):
    '''
    Get a token for utilities to access Azure.
    '''
    return call_az("az account get-access-token", locals())

