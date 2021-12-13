from .... pyaz_utils import call_az
from . import event_subscription


def show(name, resource_group, **kwargs):
    '''
    Get the details of a partner topic.
    '''
    return call_az("az eventgrid partner topic show", locals())


def delete(name, resource_group, yes=None, **kwargs):
    '''
    Delete a partner topic.
    '''
    return call_az("az eventgrid partner topic delete", locals())


def activate(name, resource_group, **kwargs):
    '''
    Activate a partner topic.
    '''
    return call_az("az eventgrid partner topic activate", locals())


def deactivate(name, resource_group, **kwargs):
    '''
    Deactivate a partner topic.
    '''
    return call_az("az eventgrid partner topic deactivate", locals())


def list(odata_query=None, resource_group=None, **kwargs):
    '''
    List available partner topics.
    '''
    return call_az("az eventgrid partner topic list", locals())

