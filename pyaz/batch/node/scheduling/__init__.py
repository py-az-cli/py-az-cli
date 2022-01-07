'''
Manage task scheduling for a Batch compute node.
'''
from .... pyaz_utils import _call_az

def disable(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None, node_disable_scheduling_option=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node on which you want to disable Task scheduling.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    - node_disable_scheduling_option -- The default value is requeue.
    '''
    return _call_az("az batch node scheduling disable", locals())


def enable(node_id, pool_id, account_endpoint=None, account_key=None, account_name=None):
    '''
    

    Required Parameters:
    - node_id -- The ID of the Compute Node on which you want to enable Task scheduling.
    - pool_id -- The ID of the Pool that contains the Compute Node.

    Optional Parameters:
    - account_endpoint -- Batch service endpoint. Alternatively, set by environment variable: AZURE_BATCH_ENDPOINT
    - account_key -- Batch account key. Alternatively, set by environment variable: AZURE_BATCH_ACCESS_KEY
    - account_name -- Batch account name. Alternatively, set by environment variable: AZURE_BATCH_ACCOUNT
    '''
    return _call_az("az batch node scheduling enable", locals())

