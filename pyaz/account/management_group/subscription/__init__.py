from .... pyaz_utils import call_az

def add(name, subscription, **kwargs):
    '''
    Add a subscription to a management group.
    '''
    return call_az("az account management-group subscription add", locals())


def remove(name, subscription, **kwargs):
    '''
    Remove an existing subscription from a management group.
    '''
    return call_az("az account management-group subscription remove", locals())

