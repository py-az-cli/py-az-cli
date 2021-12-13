from .... pyaz_utils import call_az

def list(cluster, resource_group, workspace, expiry=None, path=None, **kwargs):
    '''
    List files generated by the cluster's node setup task.
    '''
    return call_az("az batchai cluster file list", locals())

