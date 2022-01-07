'''
View Sql Vulnerability Assessment scan results.
'''
from ..... pyaz_utils import _call_az

def show(database_name, rule_id, scan_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View Sql Vulnerability Assessment scan results.

    Required Parameters:
    - database_name -- The name of the scanned database
    - rule_id -- The ID of the scanned rule. Format: "VAXXXX", where XXXX indicates the number of the rule
    - scan_id -- The ID of the scan
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql results show", locals())


def list(database_name, scan_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View all Sql Vulnerability Assessment scan results.

    Required Parameters:
    - database_name -- The name of the scanned database
    - scan_id -- The ID of the scan
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql results list", locals())

