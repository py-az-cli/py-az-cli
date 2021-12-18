from ... pyaz_utils import _call_az

def create(resource_group, workspace, location=None):
    '''
    Create a workspace.
    '''
    return _call_az("az batchai workspace create", locals())


def show(resource_group, workspace):
    '''
    Show information about a workspace.
    '''
    return _call_az("az batchai workspace show", locals())


def list(resource_group=None):
    '''
    List workspaces.
    '''
    return _call_az("az batchai workspace list", locals())


def delete(resource_group, workspace, no_wait=None, yes=None):
    '''
    Delete a workspace.
    '''
    return _call_az("az batchai workspace delete", locals())

