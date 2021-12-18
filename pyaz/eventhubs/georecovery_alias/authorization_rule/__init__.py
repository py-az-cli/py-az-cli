from .... pyaz_utils import _call_az
from . import keys


def list(alias, namespace_name, resource_group):
    '''
    List of Authorizationrule by EventHubs Namespace
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule list", locals())


def show(alias, name, namespace_name, resource_group):
    '''
    Show properties of EventHubs Geo-Disaster Recovery Configuration Alias and Namespace Authorizationrule
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule show", locals())

