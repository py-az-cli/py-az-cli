from ... pyaz_utils import call_az

def list(category=None, ids=None, refresh=None, resource_group=None, **kwargs):
    '''
    List Azure Advisor recommendations.
    '''
    return call_az("az advisor recommendation list", locals())


def disable(days=None, ids=None, name=None, resource_group=None, **kwargs):
    '''
    Disable Azure Advisor recommendations.
    '''
    return call_az("az advisor recommendation disable", locals())


def enable(ids=None, name=None, resource_group=None, **kwargs):
    '''
    Enable Azure Advisor recommendations.
    '''
    return call_az("az advisor recommendation enable", locals())

