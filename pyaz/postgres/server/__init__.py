from ... pyaz_utils import call_az
from . import ad_admin, configuration, firewall_rule, key, private_endpoint_connection, private_link_resource, replica, vnet_rule


def create(admin_password=None, admin_user=None, assign_identity=None, auto_grow=None, backup_retention=None, geo_redundant_backup=None, infrastructure_encryption=None, location=None, minimal_tls_version=None, name=None, public_network_access=None, resource_group=None, sku_name=None, ssl_enforcement=None, storage_size=None, tags=None, version=None, **kwargs):
    '''
    Create a server.
    '''
    return call_az("az postgres server create", locals())


def restore(name, resource_group, restore_point_in_time, source_server, no_wait=None, **kwargs):
    '''
    Restore a server from backup.
    '''
    return call_az("az postgres server restore", locals())


def georestore(location, name, resource_group, source_server, backup_retention=None, geo_redundant_backup=None, no_wait=None, sku_name=None, **kwargs):
    '''
    Geo-restore a server from backup.
    '''
    return call_az("az postgres server georestore", locals())


def delete(name, resource_group, yes=None, **kwargs):
    '''
    Delete a server.
    '''
    return call_az("az postgres server delete", locals())


def show(name, resource_group, **kwargs):
    '''
    Get the details of a server.
    '''
    return call_az("az postgres server show", locals())


def list(resource_group=None, **kwargs):
    '''
    List available servers.
    '''
    return call_az("az postgres server list", locals())


def update(name, resource_group, add=None, admin_password=None, assign_identity=None, auto_grow=None, backup_retention=None, force_string=None, minimal_tls_version=None, public_network_access=None, remove=None, set=None, sku_name=None, ssl_enforcement=None, storage_size=None, tags=None, **kwargs):
    '''
    Update a server.
    '''
    return call_az("az postgres server update", locals())


def wait(name, resource_group, custom=None, exists=None, interval=None, timeout=None, **kwargs):
    '''
    Wait for server to satisfy certain conditions.
    '''
    return call_az("az postgres server wait", locals())


def restart(name, resource_group, **kwargs):
    '''
    Restart a server.
    '''
    return call_az("az postgres server restart", locals())


def list_skus(location, **kwargs):
    '''
    List available sku's in the given region.
    '''
    return call_az("az postgres server list-skus", locals())


def show_connection_string(admin_password=None, admin_user=None, database_name=None, server_name=None, **kwargs):
    '''
    Show the connection strings for a PostgreSQL server database.
    '''
    return call_az("az postgres server show-connection-string", locals())

