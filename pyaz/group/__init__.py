from .. pyaz_utils import call_az
from . import deployment, lock


def delete(name, force_deletion_types=None, no_wait=None, yes=None, **kwargs):
    '''
    Delete a resource group.
    '''
    return call_az("az group delete", locals())


def show(name, **kwargs):
    return call_az("az group show", locals())


def exists(name, **kwargs):
    '''
    Check if a resource group exists.
    '''
    return call_az("az group exists", locals())


def list(tag=None, **kwargs):
    '''
    List resource groups.
    '''
    return call_az("az group list", locals())


def create(location, name, managed_by=None, tags=None, **kwargs):
    '''
    Create a new resource group.
    '''
    return call_az("az group create", locals())


def export(name, include_comments=None, include_parameter_default_value=None, resource_ids=None, skip_all_params=None, skip_resource_name_params=None, **kwargs):
    return call_az("az group export", locals())


def update(name, add=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update a resource group.
    '''
    return call_az("az group update", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the resource group is met.
    '''
    return call_az("az group wait", locals())

