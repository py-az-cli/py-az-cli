'''
Commands to work with files generated by node setup task.
'''
from .... pyaz_utils import _call_az

def list(cluster, resource_group, workspace, expiry=None, path=None):
    '''
    List files generated by the cluster's node setup task.

    Required Parameters:
    - cluster -- Name of cluster.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - workspace -- Name of workspace.

    Optional Parameters:
    - expiry -- Time in minutes for how long generated download URLs should remain valid.
    - path -- Relative path of a subfolder inside of the node setup task output directory.
    '''
    return _call_az("az batchai cluster file list", locals())

