from ... pyaz_utils import call_az
from . import file, node


def create(cluster, config_file, experiment, name, resource_group, workspace, afs_mount_path=None, afs_name=None, bfs_mount_path=None, bfs_name=None, nfs=None, nfs_mount_path=None, storage_account_key=None, storage_account_name=None, **kwargs):
    '''
    Create a job.
    '''
    return call_az("az batchai job create", locals())


def delete(experiment, name, resource_group, workspace, no_wait=None, yes=None, **kwargs):
    '''
    Delete a job.
    '''
    return call_az("az batchai job delete", locals())


def terminate(experiment, name, resource_group, workspace, no_wait=None, yes=None, **kwargs):
    '''
    Terminate a job.
    '''
    return call_az("az batchai job terminate", locals())


def show(experiment, name, resource_group, workspace, **kwargs):
    '''
    Show information about a job.
    '''
    return call_az("az batchai job show", locals())


def list(experiment, resource_group, workspace, **kwargs):
    '''
    List jobs.
    '''
    return call_az("az batchai job list", locals())


def wait(experiment, name, resource_group, workspace, interval=None, **kwargs):
    '''
    Waits for specified job completion and setups the exit code to the job's exit code.
    '''
    return call_az("az batchai job wait", locals())

