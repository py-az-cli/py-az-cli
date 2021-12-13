from ... pyaz_utils import call_az

def create(cluster_name, name, resource_group, hot_cache_period=None, no_wait=None, soft_delete_period=None, **kwargs):
    '''
    Create a Kusto database.
    '''
    return call_az("az kusto database create", locals())


def delete(cluster_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete a Kusto database.
    '''
    return call_az("az kusto database delete", locals())


def update(cluster_name, name, resource_group, soft_delete_period, add=None, force_string=None, hot_cache_period=None, no_wait=None, remove=None, set=None, **kwargs):
    '''
    Update a Kusto database.
    '''
    return call_az("az kusto database update", locals())


def list(cluster_name, resource_group, **kwargs):
    '''
    List a Kusto database.
    '''
    return call_az("az kusto database list", locals())


def show(cluster_name, name, resource_group, **kwargs):
    '''
    Get a Kusto database.
    '''
    return call_az("az kusto database show", locals())


def wait(cluster_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Wait for a managed Kusto database to reach a desired state.
    '''
    return call_az("az kusto database wait", locals())

