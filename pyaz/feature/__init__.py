from .. pyaz_utils import call_az
from . import registration


def list(namespace=None, **kwargs):
    '''
    List preview features.
    '''
    return call_az("az feature list", locals())


def show(name, namespace, **kwargs):
    return call_az("az feature show", locals())


def register(name, namespace, **kwargs):
    '''
    register a preview feature.
    '''
    return call_az("az feature register", locals())


def unregister(name, namespace, **kwargs):
    '''
    unregister a preview feature.
    '''
    return call_az("az feature unregister", locals())

