from ..... pyaz_utils import call_az

def show(database_name, scan_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None, **kwargs):
    '''
    View Sql Vulnerability Assessment scan summaries.
    '''
    return call_az("az security va sql scans show", locals())


def list(database_name, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None, **kwargs):
    '''
    List all Sql Vulnerability Assessment scan summaries.
    '''
    return call_az("az security va sql scans list", locals())

