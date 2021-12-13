from .... pyaz_utils import call_az

def create(account_name, policy, resource_group=None, **kwargs):
    '''
    Create Blob Inventory Policy for storage account.
    '''
    return call_az("az storage account blob-inventory-policy create", locals())


def update(account_name, add=None, force_string=None, remove=None, resource_group=None, set=None, **kwargs):
    '''
    Update Blob Inventory Policy associated with the specified storage account.
    '''
    return call_az("az storage account blob-inventory-policy update", locals())


def delete(account_name, resource_group=None, yes=None, **kwargs):
    '''
    Delete Blob Inventory Policy associated with the specified storage account.
    '''
    return call_az("az storage account blob-inventory-policy delete", locals())


def show(account_name, resource_group=None, **kwargs):
    '''
    Show Blob Inventory Policy properties associated with the specified storage account.
    '''
    return call_az("az storage account blob-inventory-policy show", locals())

