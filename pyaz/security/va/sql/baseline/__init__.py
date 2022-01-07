'''
View and manage Sql Vulnerability Assessment baseline.
'''
from ..... pyaz_utils import _call_az

def show(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View Sql Vulnerability Assessment rule baseline.

    Required Parameters:
    - database_name -- The name of the scanned database
    - rule_id -- The ID of the scanned rule. Format: "VAXXXX", where XXXX indicates the number of the rule
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql baseline show", locals())


def list(database_name, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    View Sql Vulnerability Assessment baseline for all rules.

    Required Parameters:
    - database_name -- The name of the scanned database
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql baseline list", locals())


def delete(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, vm_name=None, vm_uuid=None):
    '''
    Delete Sql Vulnerability Assessment rule baseline.

    Required Parameters:
    - database_name -- The name of the scanned database
    - rule_id -- The ID of the scanned rule. Format: "VAXXXX", where XXXX indicates the number of the rule
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql baseline delete", locals())


def update(database_name, rule_id, server_name, vm_resource_id, workspace_id, agent_id=None, baseline=None, latest=None, vm_name=None, vm_uuid=None):
    '''
    Update Sql Vulnerability Assessment rule baseline. Replaces the current rule baseline.

    Required Parameters:
    - database_name -- The name of the scanned database
    - rule_id -- The ID of the scanned rule. Format: "VAXXXX", where XXXX indicates the number of the rule
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - baseline -- Baseline records to be set. The following example will set a baseline with two records: --baseline line1_w1 line1_w2 line1_w3 --baseline line2_w1 line2_w2 line2_w3
    - latest -- Use this argument without parameters to set baseline upon latest scan results
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql baseline update", locals())


def set(database_name, server_name, vm_resource_id, workspace_id, agent_id=None, baseline=None, latest=None, vm_name=None, vm_uuid=None):
    '''
    Sets Sql Vulnerability Assessment baseline. Replaces the current baseline.

    Required Parameters:
    - database_name -- The name of the scanned database
    - server_name -- The name of the scanned server
    - vm_resource_id -- Resource ID of the scanned machine. For On-Premise machines, please provide your workspace resource ID
    - workspace_id -- The ID of the workspace connected to the scanned machine

    Optional Parameters:
    - agent_id -- Provide the ID of the agent on the scanned machine, for On-Premise resources only
    - baseline -- Baseline records to be set. The following example will set a baseline for two rules: --baseline rule=VA1111 line1_w1 line1_w2 --baseline rule=VA2222 line1_w1 line1_w2 line1_w3 --baseline rule=VA1111 line2_w1 line2_w2
    - latest -- Use this argument without parameters to set baseline upon latest scan results
    - vm_name -- Provide the name of the machine, for On-Premise resources only
    - vm_uuid -- Provide the UUID of the scanned machine, for On-Premise resources only
    '''
    return _call_az("az security va sql baseline set", locals())

