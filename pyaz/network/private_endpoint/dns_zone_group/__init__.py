from .... pyaz_utils import call_az

def create(endpoint_name, name, private_dns_zone, resource_group, zone_name, **kwargs):
    '''
    Create a private endpoint dns zone group.
    '''
    return call_az("az network private-endpoint dns-zone-group create", locals())


def add(endpoint_name, name, private_dns_zone, resource_group, zone_name, **kwargs):
    '''
    Add a private endpoint dns zone into a dns zone group.
    '''
    return call_az("az network private-endpoint dns-zone-group add", locals())


def remove(endpoint_name, name, resource_group, zone_name, **kwargs):
    '''
    Remove a private endpoint dns zone into a dns zone group.
    '''
    return call_az("az network private-endpoint dns-zone-group remove", locals())


def delete(endpoint_name, name, resource_group, **kwargs):
    '''
    Delete a private endpoint dns zone group.
    '''
    return call_az("az network private-endpoint dns-zone-group delete", locals())


def show(endpoint_name, name, resource_group, **kwargs):
    '''
    Show a private endpoint dns zone group.
    '''
    return call_az("az network private-endpoint dns-zone-group show", locals())


def list(endpoint_name, resource_group, **kwargs):
    '''
    List all private endpoint dns zone groups.
    '''
    return call_az("az network private-endpoint dns-zone-group list", locals())

