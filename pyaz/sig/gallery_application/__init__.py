from ... pyaz_utils import call_az
from . import version


def list(gallery_name, resource_group, **kwargs):
    return call_az("az sig gallery-application list", locals())


def show(gallery_name, name, resource_group, **kwargs):
    return call_az("az sig gallery-application show", locals())


def create(gallery_name, name, os_type, resource_group, description=None, location=None, no_wait=None, tags=None, **kwargs):
    '''
    Create a gallery Application Definition.
    '''
    return call_az("az sig gallery-application create", locals())


def update(gallery_name, name, resource_group, description=None, location=None, no_wait=None, tags=None, **kwargs):
    '''
    Update a gallery Application Definition.
    '''
    return call_az("az sig gallery-application update", locals())


def delete(gallery_name, name, resource_group, no_wait=None, yes=None, **kwargs):
    return call_az("az sig gallery-application delete", locals())


def wait(gallery_name, name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the sig gallery-application is met.
    '''
    return call_az("az sig gallery-application wait", locals())

