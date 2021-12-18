from ... pyaz_utils import _call_az

def show(resource_group, rollout_name, retry_attempt=None):
    '''
    Gets the rollout.
    '''
    return _call_az("az deploymentmanager rollout show", locals())


def list(resource_group):
    '''
    List all rollouts in a resource group
    '''
    return _call_az("az deploymentmanager rollout list", locals())


def stop(resource_group, rollout_name, yes=None):
    '''
    Stop the rollout.
    '''
    return _call_az("az deploymentmanager rollout stop", locals())


def restart(resource_group, rollout_name, skip_succeeded=None, yes=None):
    '''
    Restarts the rollout.
    '''
    return _call_az("az deploymentmanager rollout restart", locals())


def delete(resource_group, rollout_name):
    return _call_az("az deploymentmanager rollout delete", locals())

