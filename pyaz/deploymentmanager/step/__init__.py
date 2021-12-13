from ... pyaz_utils import call_az

def create(resource_group, duration=None, location=None, step=None, step_name=None, tags=None, **kwargs):
    '''
    Creates the step.
    '''
    return call_az("az deploymentmanager step create", locals())


def delete(resource_group, step_name, **kwargs):
    return call_az("az deploymentmanager step delete", locals())


def show(resource_group, step_name, **kwargs):
    '''
    Get the details of the step.
    '''
    return call_az("az deploymentmanager step show", locals())


def list(resource_group, **kwargs):
    '''
    List all steps in a resource group.
    '''
    return call_az("az deploymentmanager step list", locals())


def update(resource_group, step_name, add=None, duration=None, force_string=None, remove=None, set=None, step=None, tags=None, **kwargs):
    '''
    Updates the step.
    '''
    return call_az("az deploymentmanager step update", locals())

