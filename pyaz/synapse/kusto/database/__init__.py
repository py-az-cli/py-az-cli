from .... pyaz_utils import call_az

def list(kusto_pool_name, resource_group, workspace_name, **kwargs):
    '''
    Returns the list of databases of the given Kusto pool.
    '''
    return call_az("az synapse kusto database list", locals())


def show(database_name, kusto_pool_name, resource_group, workspace_name, **kwargs):
    '''
    Returns a database.
    '''
    return call_az("az synapse kusto database show", locals())


def create(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, read_write_database=None, **kwargs):
    '''
    Create a database.
    '''
    return call_az("az synapse kusto database create", locals())


def update(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, read_write_database=None, **kwargs):
    '''
    Updates a database.
    '''
    return call_az("az synapse kusto database update", locals())


def delete(database_name, kusto_pool_name, resource_group, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Deletes the database with the given name.
    '''
    return call_az("az synapse kusto database delete", locals())


def wait(database_name, kusto_pool_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto database is met.
    '''
    return call_az("az synapse kusto database wait", locals())

