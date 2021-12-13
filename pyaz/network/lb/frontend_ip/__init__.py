from .... pyaz_utils import call_az

def list(lb_name, resource_group, **kwargs):
    '''
    List frontend IP addresses.
    '''
    return call_az("az network lb frontend-ip list", locals())


def show(lb_name, name, resource_group, **kwargs):
    '''
    Get the details of a frontend IP address.
    '''
    return call_az("az network lb frontend-ip show", locals())


def delete(lb_name, name, resource_group, **kwargs):
    '''
    Delete a frontend IP address.
    '''
    return call_az("az network lb frontend-ip delete", locals())


def create(lb_name, name, resource_group, private_ip_address=None, private_ip_address_version=None, public_ip_address=None, public_ip_prefix=None, subnet=None, vnet_name=None, zone=None, **kwargs):
    '''
    Create a frontend IP address.
    '''
    return call_az("az network lb frontend-ip create", locals())


def update(lb_name, name, resource_group, add=None, force_string=None, gateway_lb=None, private_ip_address=None, public_ip_address=None, public_ip_prefix=None, remove=None, set=None, subnet=None, vnet_name=None, **kwargs):
    '''
    Update a frontend IP address.
    '''
    return call_az("az network lb frontend-ip update", locals())

