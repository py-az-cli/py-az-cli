from ... pyaz_utils import call_az
from . import dns_zone_group


def create(connection_name, name, private_connection_resource_id, resource_group, subnet, edge_zone=None, group_id=None, location=None, manual_request=None, request_message=None, tags=None, vnet_name=None, **kwargs):
    '''
    Create a private endpoint.
    '''
    return call_az("az network private-endpoint create", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete a private endpoint.
    '''
    return call_az("az network private-endpoint delete", locals())


def list(resource_group=None, **kwargs):
    '''
    List private endpoints.
    '''
    return call_az("az network private-endpoint list", locals())


def show(name, resource_group, **kwargs):
    '''
    Get the details of a private endpoint.
    '''
    return call_az("az network private-endpoint show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, request_message=None, set=None, tags=None, **kwargs):
    '''
    Update a private endpoint.
    '''
    return call_az("az network private-endpoint update", locals())


def list_types(location, **kwargs):
    return call_az("az network private-endpoint list-types", locals())

