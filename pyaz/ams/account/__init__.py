from ... pyaz_utils import call_az
from . import encryption, mru, sp, storage


def show(name, resource_group=None, **kwargs):
    '''
    Show the details of an Azure Media Services account.
    '''
    return call_az("az ams account show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete an Azure Media Services account.
    '''
    return call_az("az ams account delete", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update the details of an Azure Media Services account.
    '''
    return call_az("az ams account update", locals())


def list(resource_group=None, **kwargs):
    '''
    List Azure Media Services accounts for the entire subscription.
    '''
    return call_az("az ams account list", locals())


def create(name, resource_group, storage_account, location=None, mi_system_assigned=None, tags=None, **kwargs):
    '''
    Create an Azure Media Services account.
    '''
    return call_az("az ams account create", locals())


def check_name(name, location=None, **kwargs):
    '''
    Checks whether the Media Service resource name is available.
    '''
    return call_az("az ams account check-name", locals())

