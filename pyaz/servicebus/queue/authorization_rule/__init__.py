from .... pyaz_utils import call_az
from . import keys


def create(name, namespace_name, queue_name, resource_group, rights=None, **kwargs):
    '''
    Create Authorization Rule for the given Service Bus Queue.
    '''
    return call_az("az servicebus queue authorization-rule create", locals())


def show(name, namespace_name, queue_name, resource_group, **kwargs):
    '''
    show properties of Authorization Rule for the given Service Bus Queue.
    '''
    return call_az("az servicebus queue authorization-rule show", locals())


def list(namespace_name, queue_name, resource_group, **kwargs):
    '''
    List of Authorization Rule by Service Bus Queue.
    '''
    return call_az("az servicebus queue authorization-rule list", locals())


def delete(name, namespace_name, queue_name, resource_group, **kwargs):
    '''
    Delete the Authorization Rule of Service Bus Queue
    '''
    return call_az("az servicebus queue authorization-rule delete", locals())


def update(name, namespace_name, queue_name, resource_group, rights, add=None, force_string=None, remove=None, set=None, **kwargs):
    '''
    Update Authorization Rule for the given Service Bus Queue.
    '''
    return call_az("az servicebus queue authorization-rule update", locals())

