from ... pyaz_utils import call_az

def create(file, name, workspace_name, no_wait=None, **kwargs):
    '''
    Create a data flow.
    '''
    return call_az("az synapse data-flow create", locals())


def set(file, name, workspace_name, no_wait=None, **kwargs):
    '''
    Set an exist data flow.
    '''
    return call_az("az synapse data-flow set", locals())


def list(workspace_name, **kwargs):
    '''
    List data flows.
    '''
    return call_az("az synapse data-flow list", locals())


def show(name, workspace_name, **kwargs):
    '''
    Get a data flow.
    '''
    return call_az("az synapse data-flow show", locals())


def delete(name, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Delete a data flow.
    '''
    return call_az("az synapse data-flow delete", locals())

