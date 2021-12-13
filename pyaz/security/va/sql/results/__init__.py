from ..... pyaz_utils import call_az

def show(database_name, rule_id, scan_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None, **kwargs):
    '''
    View Sql Vulnerability Assessment scan results.
    '''
    return call_az("az security va sql results show", locals())


def list(database_name, scan_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None, **kwargs):
    '''
    View all Sql Vulnerability Assessment scan results.
    '''
    return call_az("az security va sql results list", locals())

