from ..... pyaz_utils import call_az

def list(resource_group, workspace_name, **kwargs):
    '''
    List all the tables for the given Log Analytics workspace.
    '''
    return call_az("az monitor log-analytics workspace table list", locals())


def show(name, resource_group, workspace_name, **kwargs):
    '''
    Get a Log Analytics workspace table.
    '''
    return call_az("az monitor log-analytics workspace table show", locals())


def update(name, resource_group, retention_time, workspace_name, **kwargs):
    '''
    Update the properties of a Log Analytics workspace table, currently only support updating retention time.
    '''
    return call_az("az monitor log-analytics workspace table update", locals())

