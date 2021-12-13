from .... pyaz_utils import call_az

def list(gateway_name, resource_group, **kwargs):
    '''
    List SSL certificates.
    '''
    return call_az("az network application-gateway ssl-cert list", locals())


def show(gateway_name, name, resource_group, **kwargs):
    '''
    Get the details of an SSL certificate.
    '''
    return call_az("az network application-gateway ssl-cert show", locals())


def delete(gateway_name, name, resource_group, no_wait=None, **kwargs):
    '''
    Delete an SSL certificate.
    '''
    return call_az("az network application-gateway ssl-cert delete", locals())


def create(gateway_name, name, resource_group, cert_file=None, cert_password=None, key_vault_secret_id=None, no_wait=None, **kwargs):
    '''
    Upload an SSL certificate.
    '''
    return call_az("az network application-gateway ssl-cert create", locals())


def update(gateway_name, name, resource_group, add=None, cert_file=None, cert_password=None, force_string=None, key_vault_secret_id=None, no_wait=None, remove=None, set=None, **kwargs):
    '''
    Update an SSL certificate.
    '''
    return call_az("az network application-gateway ssl-cert update", locals())

