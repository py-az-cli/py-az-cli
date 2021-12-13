from .... pyaz_utils import call_az
from . import audit_policy, classification, tde, threat_policy


def show(name, resource_group, workspace_name, **kwargs):
    '''
    Get a SQL pool.
    '''
    return call_az("az synapse sql pool show", locals())


def list(resource_group, workspace_name, **kwargs):
    '''
    List all SQL pools.
    '''
    return call_az("az synapse sql pool list", locals())


def create(name, performance_level, resource_group, workspace_name, no_wait=None, tags=None, **kwargs):
    '''
    Create a SQL pool.
    '''
    return call_az("az synapse sql pool create", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Delete a SQL pool.
    '''
    return call_az("az synapse sql pool delete", locals())


def update(name, resource_group, workspace_name, performance_level=None, tags=None, **kwargs):
    '''
    Update a SQL pool.
    '''
    return call_az("az synapse sql pool update", locals())


def pause(name, resource_group, workspace_name, **kwargs):
    '''
    Pause a SQL pool.
    '''
    return call_az("az synapse sql pool pause", locals())


def resume(name, resource_group, workspace_name, **kwargs):
    '''
    Resume a SQL pool.
    '''
    return call_az("az synapse sql pool resume", locals())


def restore(dest_name, name, resource_group, workspace_name, deleted_time=None, performance_level=None, time=None, **kwargs):
    '''
    Create a new SQL pool by restoring from a backup.
    '''
    return call_az("az synapse sql pool restore", locals())


def show_connection_string(client, auth_type=None, name=None, workspace_name=None, **kwargs):
    '''
    Generate a connection string to a SQL pool.
    '''
    return call_az("az synapse sql pool show-connection-string", locals())


def wait(resource_group, sql_pool_name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of a SQL pool is met.
    '''
    return call_az("az synapse sql pool wait", locals())


def list_deleted(resource_group, workspace_name, **kwargs):
    '''
    List all deleted SQL pools.
    '''
    return call_az("az synapse sql pool list-deleted", locals())

