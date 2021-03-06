from .... pyaz_utils import _call_az

def create(endpoint_name, name, private_dns_zone, resource_group, zone_name):
    '''
    Create a private endpoint dns zone group.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - name -- Name of the private dns zone group.
    - private_dns_zone -- Name or ID of the private dns zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- Name of the private dns zone.
    '''
    return _call_az("az network private-endpoint dns-zone-group create", locals())


def add(endpoint_name, name, private_dns_zone, resource_group, zone_name):
    '''
    Add a private endpoint dns zone into a dns zone group.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - name -- Name of the private dns zone group.
    - private_dns_zone -- Name or ID of the private dns zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- Name of the private dns zone.
    '''
    return _call_az("az network private-endpoint dns-zone-group add", locals())


def remove(endpoint_name, name, resource_group, zone_name):
    '''
    Remove a private endpoint dns zone into a dns zone group.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - name -- Name of the private dns zone group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- Name of the private dns zone.
    '''
    return _call_az("az network private-endpoint dns-zone-group remove", locals())


def delete(endpoint_name, name, resource_group):
    '''
    Delete a private endpoint dns zone group.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - name -- Name of the private dns zone group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint dns-zone-group delete", locals())


def show(endpoint_name, name, resource_group):
    '''
    Show a private endpoint dns zone group.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - name -- Name of the private dns zone group.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint dns-zone-group show", locals())


def list(endpoint_name, resource_group):
    '''
    List all private endpoint dns zone groups.

    Required Parameters:
    - endpoint_name -- Name of the private endpoint.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az network private-endpoint dns-zone-group list", locals())

