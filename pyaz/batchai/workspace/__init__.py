from ... pyaz_utils import call_az

def create(resource_group, workspace, location=None, **kwargs):
    '''
    Create a workspace.
    '''
    return call_az("az batchai workspace create", locals())


def show(resource_group, workspace, **kwargs):
    '''
    Show information about a workspace.
    '''
    return call_az("az batchai workspace show", locals())


def list(resource_group=None, **kwargs):
    '''
    List workspaces.
    '''
    return call_az("az batchai workspace list", locals())


def delete(resource_group, workspace, no_wait=None, yes=None, **kwargs):
    '''
    Delete a workspace.
    '''
    return call_az("az batchai workspace delete", locals())

