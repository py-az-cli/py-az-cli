from .... pyaz_utils import call_az

def create(address_prefix, appliance_name, name, resource_group, allow=None, default=None, optimize=None, **kwargs):
    '''
    Create an Azure network virtual appliance site.
    '''
    return call_az("az network virtual-appliance site create", locals())


def update(address_prefix, appliance_name, name, resource_group, add=None, allow=None, default=None, force_string=None, optimize=None, remove=None, set=None, **kwargs):
    '''
    Update an Azure network virtual appliance site.
    '''
    return call_az("az network virtual-appliance site update", locals())


def show(appliance_name, name, resource_group, **kwargs):
    '''
    Show the detail of an Azure network virtual appliance site.
    '''
    return call_az("az network virtual-appliance site show", locals())


def delete(appliance_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete an Azure network virtual appliance site.
    '''
    return call_az("az network virtual-appliance site delete", locals())


def list(appliance_name, resource_group, **kwargs):
    '''
    List all Azure network virtual appliance site.
    '''
    return call_az("az network virtual-appliance site list", locals())

