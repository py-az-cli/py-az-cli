from .... pyaz_utils import call_az

def list(gateway_name, resource_group, **kwargs):
    '''
    List frontend ports.
    '''
    return call_az("az network application-gateway frontend-port list", locals())


def show(gateway_name, name, resource_group, **kwargs):
    '''
    Get the details of a frontend port.
    '''
    return call_az("az network application-gateway frontend-port show", locals())


def delete(gateway_name, name, resource_group, no_wait=None, **kwargs):
    '''
    Delete a frontend port.
    '''
    return call_az("az network application-gateway frontend-port delete", locals())


def create(gateway_name, name, port, resource_group, no_wait=None, **kwargs):
    '''
    Create a frontend port.
    '''
    return call_az("az network application-gateway frontend-port create", locals())


def update(gateway_name, name, resource_group, add=None, force_string=None, no_wait=None, port=None, remove=None, set=None, **kwargs):
    '''
    Update a frontend port.
    '''
    return call_az("az network application-gateway frontend-port update", locals())

