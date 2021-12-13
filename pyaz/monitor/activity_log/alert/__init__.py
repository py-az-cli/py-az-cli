from .... pyaz_utils import call_az
from . import action_group, scope


def list(resource_group=None, **kwargs):
    '''
    List activity log alerts under a resource group or the current subscription.
    '''
    return call_az("az monitor activity-log alert list", locals())


def create(name, resource_group, action_group=None, condition=None, description=None, disable=None, scope=None, tags=None, webhook_properties=None, **kwargs):
    '''
    Create a default activity log alert
    '''
    return call_az("az monitor activity-log alert create", locals())


def show(name, resource_group, **kwargs):
    return call_az("az monitor activity-log alert show", locals())


def delete(name, resource_group, **kwargs):
    return call_az("az monitor activity-log alert delete", locals())


def update(name, resource_group, add=None, condition=None, description=None, enabled=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update the details of this activity log alert
    '''
    return call_az("az monitor activity-log alert update", locals())

