from .... pyaz_utils import call_az

def list(kusto_pool_name, resource_group, workspace_name, **kwargs):
    '''
    Lists all Kusto pool principalAssignments.
    '''
    return call_az("az synapse kusto pool-principal-assignment list", locals())


def show(kusto_pool_name, principal_assignment_name, resource_group, workspace_name, **kwargs):
    '''
    Gets a Kusto pool principalAssignment.
    '''
    return call_az("az synapse kusto pool-principal-assignment show", locals())


def create(kusto_pool_name, principal_assignment_name, resource_group, workspace_name, no_wait=None, principal_id=None, principal_type=None, role=None, tenant_id=None, **kwargs):
    '''
    Create a Kusto pool principalAssignment.
    '''
    return call_az("az synapse kusto pool-principal-assignment create", locals())


def update(kusto_pool_name, principal_assignment_name, resource_group, workspace_name, add=None, force_string=None, no_wait=None, principal_id=None, principal_type=None, remove=None, role=None, set=None, tenant_id=None, **kwargs):
    '''
    Update a Kusto pool principalAssignment.
    '''
    return call_az("az synapse kusto pool-principal-assignment update", locals())


def delete(kusto_pool_name, principal_assignment_name, resource_group, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Deletes a Kusto pool principalAssignment.
    '''
    return call_az("az synapse kusto pool-principal-assignment delete", locals())


def wait(kusto_pool_name, principal_assignment_name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the synapse kusto pool-principal-assignment is met.
    '''
    return call_az("az synapse kusto pool-principal-assignment wait", locals())

