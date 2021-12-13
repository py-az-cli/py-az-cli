from ... pyaz_utils import call_az

def show(name, resource_group=None, **kwargs):
    '''
    Get the login credentials for an Azure Container Registry.
    '''
    return call_az("az acr credential show", locals())


def renew(name, password_name, resource_group=None, **kwargs):
    '''
    Regenerate login credentials for an Azure Container Registry.
    '''
    return call_az("az acr credential renew", locals())

