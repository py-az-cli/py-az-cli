from .... pyaz_utils import call_az

def create(application_name, name, package_file, resource_group, version_name, **kwargs):
    '''
    Create a Batch application package record and activate it.
    '''
    return call_az("az batch application package create", locals())


def delete(application_name, name, resource_group, version_name, yes=None, **kwargs):
    return call_az("az batch application package delete", locals())


def show(application_name, name, resource_group, version_name, **kwargs):
    return call_az("az batch application package show", locals())


def activate(application_name, format, name, resource_group, version_name, **kwargs):
    '''
    Activates a Batch application package.
    '''
    return call_az("az batch application package activate", locals())


def list(application_name, name, resource_group, maxresults=None, **kwargs):
    return call_az("az batch application package list", locals())

