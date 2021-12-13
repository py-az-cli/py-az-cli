from ... pyaz_utils import call_az

def create(file, name, workspace_name, no_wait=None, **kwargs):
    '''
    Create a dataset.
    '''
    return call_az("az synapse dataset create", locals())


def set(file, name, workspace_name, no_wait=None, **kwargs):
    '''
    Update an exist dataset.
    '''
    return call_az("az synapse dataset set", locals())


def update(file, name, workspace_name, no_wait=None, **kwargs):
    '''
    Update an exist dataset.
    '''
    return call_az("az synapse dataset update", locals())


def list(workspace_name, **kwargs):
    '''
    List datasets.
    '''
    return call_az("az synapse dataset list", locals())


def show(name, workspace_name, **kwargs):
    '''
    Get a dataset.
    '''
    return call_az("az synapse dataset show", locals())


def delete(name, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Delete a dataset.
    '''
    return call_az("az synapse dataset delete", locals())

