from .... pyaz_utils import _call_az

def add(name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Add a network rule.
    '''
    return _call_az("az cognitiveservices account network-rule add", locals())


def list(name, resource_group):
    '''
    List network rules.
    '''
    return _call_az("az cognitiveservices account network-rule list", locals())


def remove(name, resource_group, ip_address=None, subnet=None, vnet_name=None):
    '''
    Remove a network rule.
    '''
    return _call_az("az cognitiveservices account network-rule remove", locals())

