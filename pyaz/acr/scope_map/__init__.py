from ... pyaz_utils import call_az

def create(name, registry, description=None, gateway=None, repository=None, resource_group=None, **kwargs):
    '''
    Create a scope map for an Azure Container Registry.
    '''
    return call_az("az acr scope-map create", locals())


def delete(name, registry, resource_group=None, yes=None, **kwargs):
    '''
    Delete a scope map for an Azure Container Registry.
    '''
    return call_az("az acr scope-map delete", locals())


def update(name, registry, add_gateway=None, add_repository=None, description=None, remove_gateway=None, remove_repository=None, resource_group=None, **kwargs):
    '''
    Update a scope map for an Azure Container Registry.
    '''
    return call_az("az acr scope-map update", locals())


def show(name, registry, resource_group=None, **kwargs):
    '''
    Show details and attributes of a scope map for an Azure Container Registry.
    '''
    return call_az("az acr scope-map show", locals())


def list(registry, resource_group=None, **kwargs):
    '''
    List all scope maps for an Azure Container Registry.
    '''
    return call_az("az acr scope-map list", locals())

