from .... pyaz_utils import call_az

def create(cluster_name, days, resource_group, time, workernode_count, no_wait=None, **kwargs):
    '''
    Add a new schedule condition.
    '''
    return call_az("az hdinsight autoscale condition create", locals())


def update(cluster_name, index, resource_group, days=None, no_wait=None, time=None, workernode_count=None, **kwargs):
    '''
    Update a schedule condition.
    '''
    return call_az("az hdinsight autoscale condition update", locals())


def list(cluster_name, resource_group, **kwargs):
    '''
    List all schedule conditions.
    '''
    return call_az("az hdinsight autoscale condition list", locals())


def delete(cluster_name, index, resource_group, no_wait=None, yes=None, **kwargs):
    '''
    Delete schedule condition.
    '''
    return call_az("az hdinsight autoscale condition delete", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until an operation is complete.
    '''
    return call_az("az hdinsight autoscale condition wait", locals())

