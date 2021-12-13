from .... pyaz_utils import call_az

def create(account_name, name, subnet, resource_group=None, vnet_name=None, **kwargs):
    '''
    Creates a virtual network rule in a Data Lake Store account.
    '''
    return call_az("az dls account network-rule create", locals())


def update(account_name, name, subnet, add=None, force_string=None, remove=None, resource_group=None, set=None, vnet_name=None, **kwargs):
    '''
    Updates a virtual network rule in a Data Lake Store account.
    '''
    return call_az("az dls account network-rule update", locals())


def list(account_name, resource_group=None, **kwargs):
    '''
    Lists virtual network rules in a Data Lake Store account.
    '''
    return call_az("az dls account network-rule list", locals())


def show(account_name, name, resource_group=None, **kwargs):
    '''
    Get the details of a virtual network rule in a Data Lake Store account.
    '''
    return call_az("az dls account network-rule show", locals())


def delete(account_name, name, resource_group=None, **kwargs):
    '''
    Deletes a virtual network rule in a Data Lake Store account.
    '''
    return call_az("az dls account network-rule delete", locals())

