from ... pyaz_utils import call_az

def show(pe_name, workspace_name, **kwargs):
    '''
    Get a synapse managed private endpoints.
    '''
    return call_az("az synapse managed-private-endpoints show", locals())


def create(group_Id, pe_name, resource_id, workspace_name, **kwargs):
    '''
    Create a synapse managed private endpoints.
    '''
    return call_az("az synapse managed-private-endpoints create", locals())


def list(workspace_name, **kwargs):
    '''
    List synapse managed private endpoints in a workspace.
    '''
    return call_az("az synapse managed-private-endpoints list", locals())


def delete(pe_name, workspace_name, yes=None, **kwargs):
    '''
    delete synapse managed private endpoints in a workspace.
    '''
    return call_az("az synapse managed-private-endpoints delete", locals())

