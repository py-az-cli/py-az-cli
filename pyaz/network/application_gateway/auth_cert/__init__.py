from .... pyaz_utils import call_az

def list(gateway_name, resource_group, **kwargs):
    '''
    List authorization certificates.
    '''
    return call_az("az network application-gateway auth-cert list", locals())


def show(gateway_name, name, resource_group, **kwargs):
    '''
    Show an authorization certificate.
    '''
    return call_az("az network application-gateway auth-cert show", locals())


def delete(gateway_name, name, resource_group, no_wait=None, **kwargs):
    '''
    Delete an authorization certificate.
    '''
    return call_az("az network application-gateway auth-cert delete", locals())


def create(cert_file, gateway_name, name, resource_group, no_wait=None, **kwargs):
    '''
    Create an authorization certificate.
    '''
    return call_az("az network application-gateway auth-cert create", locals())


def update(cert_file, gateway_name, name, resource_group, add=None, force_string=None, no_wait=None, remove=None, set=None, **kwargs):
    '''
    Update an authorization certificate.
    '''
    return call_az("az network application-gateway auth-cert update", locals())

