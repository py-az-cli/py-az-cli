from ..... pyaz_utils import call_az

def list(resource_group, workspace_name, **kwargs):
    '''
    List all data export ruleses for a given workspace.
    '''
    return call_az("az monitor log-analytics workspace data-export list", locals())


def show(name, resource_group, workspace_name, **kwargs):
    '''
    Show a data export rule for a given workspace.
    '''
    return call_az("az monitor log-analytics workspace data-export show", locals())


def create(destination, name, resource_group, tables, workspace_name, enable=None, **kwargs):
    '''
    Create a data export rule for a given workspace.
    '''
    return call_az("az monitor log-analytics workspace data-export create", locals())


def update(name, resource_group, tables, workspace_name, add=None, destination=None, enable=None, force_string=None, remove=None, set=None, **kwargs):
    '''
    Update a data export rule for a given workspace.
    '''
    return call_az("az monitor log-analytics workspace data-export update", locals())


def delete(name, resource_group, workspace_name, yes=None, **kwargs):
    '''
    Delete a data export rule for a given workspace.
    '''
    return call_az("az monitor log-analytics workspace data-export delete", locals())

