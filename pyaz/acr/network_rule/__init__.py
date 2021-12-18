from ... pyaz_utils import _call_az

def list(name, resource_group=None):
    '''
    List network rules.
    '''
    return _call_az("az acr network-rule list", locals())


def add(name, ip_address=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    Add a network rule.
    '''
    return _call_az("az acr network-rule add", locals())


def remove(name, ip_address=None, resource_group=None, subnet=None, vnet_name=None):
    '''
    Remove a network rule.
    '''
    return _call_az("az acr network-rule remove", locals())

