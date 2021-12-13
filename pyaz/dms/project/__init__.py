from ... pyaz_utils import call_az
from . import task


def create(location, name, resource_group, service_name, source_platform, target_platform, tags=None, **kwargs):
    '''
    Create a migration project which can contain multiple tasks.
    '''
    return call_az("az dms project create", locals())


def delete(name, resource_group, service_name, delete_running_tasks=None, yes=None, **kwargs):
    '''
    Delete a project.
    '''
    return call_az("az dms project delete", locals())


def list(resource_group, service_name, **kwargs):
    '''
    List the projects within an instance of DMS.
    '''
    return call_az("az dms project list", locals())


def show(name, resource_group, service_name, **kwargs):
    '''
    Show the details of a migration project.
    '''
    return call_az("az dms project show", locals())


def check_name(name, resource_group, service_name, **kwargs):
    '''
    Check if a given project name is available within a given instance of DMS as well as the name's validity.
    '''
    return call_az("az dms project check-name", locals())

