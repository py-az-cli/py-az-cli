from .... pyaz_utils import call_az

def show(registry, resource_group=None, **kwargs):
    '''
    Show the configured retention policy for an Azure Container Registry.
    '''
    return call_az("az acr config retention show", locals())


def update(registry, type, days=None, resource_group=None, status=None, **kwargs):
    '''
    Update retention policy for an Azure Container Registry.
    '''
    return call_az("az acr config retention update", locals())

