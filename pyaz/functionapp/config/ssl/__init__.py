from .... pyaz_utils import call_az

def upload(certificate_file, certificate_password, name, resource_group, slot=None, **kwargs):
    '''
    Upload an SSL certificate to a function app.
    '''
    return call_az("az functionapp config ssl upload", locals())


def list(resource_group, **kwargs):
    '''
    List SSL certificates for a function app.
    '''
    return call_az("az functionapp config ssl list", locals())


def show(certificate_name, resource_group, **kwargs):
    '''
    Show the details of an SSL certificate for a function app.
    '''
    return call_az("az functionapp config ssl show", locals())


def bind(certificate_thumbprint, name, resource_group, ssl_type, slot=None, **kwargs):
    '''
    Bind an SSL certificate to a function app.
    '''
    return call_az("az functionapp config ssl bind", locals())


def unbind(certificate_thumbprint, name, resource_group, slot=None, **kwargs):
    '''
    Unbind an SSL certificate from a function app.
    '''
    return call_az("az functionapp config ssl unbind", locals())


def delete(certificate_thumbprint, resource_group, **kwargs):
    '''
    Delete an SSL certificate from a function app.
    '''
    return call_az("az functionapp config ssl delete", locals())


def import_(key_vault, key_vault_certificate_name, name, resource_group, **kwargs):
    '''
    Import an SSL certificate to a function app from Key Vault.
    '''
    return call_az("az functionapp config ssl import", locals())


def create(hostname, name, resource_group, slot=None, **kwargs):
    '''
    Create a Managed Certificate for a hostname in a function app.
    '''
    return call_az("az functionapp config ssl create", locals())

