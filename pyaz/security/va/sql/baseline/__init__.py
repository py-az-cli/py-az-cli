from ..... pyaz_utils import call_az

def show(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View Sql Vulnerability Assessment rule baseline.
    '''
    return call_az("az security va sql baseline show", locals())


def list(database_name, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View Sql Vulnerability Assessment baseline for all rules.
    '''
    return call_az("az security va sql baseline list", locals())


def delete(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    Delete Sql Vulnerability Assessment rule baseline.
    '''
    return call_az("az security va sql baseline delete", locals())


def update(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, baseline=None, latest=None, vm_name=None, vm_uuid=None):
    '''
    Update Sql Vulnerability Assessment rule baseline. Replaces the current rule baseline.
    '''
    return call_az("az security va sql baseline update", locals())


def set(database_name, server_name, vm_resource_id, workspace_id, agent_id=None, baseline=None, latest=None, vm_name=None, vm_uuid=None):
    '''
    Sets Sql Vulnerability Assessment baseline. Replaces the current baseline.
    '''
    return call_az("az security va sql baseline set", locals())

