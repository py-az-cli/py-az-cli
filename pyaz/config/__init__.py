from .. pyaz_utils import call_az
from . import param_persist


def set(local=None, **kwargs):
    '''
    Set a configuration.
    '''
    return call_az("az config set", locals())


def get(local=None, **kwargs):
    '''
    Get a configuration.
    '''
    return call_az("az config get", locals())


def unset(local=None, **kwargs):
    '''
    Unset a configuration.
    '''
    return call_az("az config unset", locals())

