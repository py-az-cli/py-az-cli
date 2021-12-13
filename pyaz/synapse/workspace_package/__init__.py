from ... pyaz_utils import call_az

def upload(package, workspace_name, no_progress=None, **kwargs):
    '''
    Upload a local workspace package file to an Azure Synapse workspace.
    '''
    return call_az("az synapse workspace-package upload", locals())


def upload_batch(source, workspace_name, no_progress=None, **kwargs):
    '''
    Upload workspace package files from a local directory to an Azure Synapse workspace.
    '''
    return call_az("az synapse workspace-package upload-batch", locals())


def list(workspace_name, **kwargs):
    '''
    List workspace packages.
    '''
    return call_az("az synapse workspace-package list", locals())


def show(package_name, workspace_name, **kwargs):
    '''
    Get a workspace package.
    '''
    return call_az("az synapse workspace-package show", locals())


def delete(package_name, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Delete a workspace package.
    '''
    return call_az("az synapse workspace-package delete", locals())

