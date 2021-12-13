from .... pyaz_utils import call_az

def create(name, resource_group, subdomain, display_name=None, location=None, no_wait=None, sku=None, template=None, **kwargs):
    '''
    Create an IoT Central application.
    '''
    return call_az("az iot central app create", locals())


def list(resource_group=None, **kwargs):
    '''
    List IoT Central applications.
    '''
    return call_az("az iot central app list", locals())


def show(name, resource_group=None, **kwargs):
    '''
    Get the details of an IoT Central application.
    '''
    return call_az("az iot central app show", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, **kwargs):
    '''
    Update metadata for an IoT Central application.
    '''
    return call_az("az iot central app update", locals())


def delete(name, resource_group, no_wait=None, yes=None, **kwargs):
    '''
    Delete an IoT Central application.
    '''
    return call_az("az iot central app delete", locals())

