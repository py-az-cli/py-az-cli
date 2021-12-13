from ... pyaz_utils import call_az

def list(name, password=None, resource_group=None, suffix=None, top=None, username=None, **kwargs):
    '''
    List repositories in an Azure Container Registry.
    '''
    return call_az("az acr repository list", locals())


def show_tags(name, repository, detail=None, orderby=None, password=None, resource_group=None, suffix=None, top=None, username=None, **kwargs):
    '''
    Show tags for a repository in an Azure Container Registry.
    '''
    return call_az("az acr repository show-tags", locals())


def show_manifests(name, repository, detail=None, orderby=None, password=None, resource_group=None, suffix=None, top=None, username=None, **kwargs):
    '''
    Show manifests of a repository in an Azure Container Registry.
    '''
    return call_az("az acr repository show-manifests", locals())


def show(name, image=None, password=None, repository=None, resource_group=None, suffix=None, username=None, **kwargs):
    '''
    Get the attributes of a repository or image in an Azure Container Registry.
    '''
    return call_az("az acr repository show", locals())


def update(name, delete_enabled=None, image=None, list_enabled=None, password=None, read_enabled=None, repository=None, resource_group=None, suffix=None, username=None, write_enabled=None, **kwargs):
    '''
    Update the attributes of a repository or image in an Azure Container Registry.
    '''
    return call_az("az acr repository update", locals())


def delete(name, image=None, password=None, repository=None, resource_group=None, suffix=None, username=None, yes=None, **kwargs):
    '''
    Delete a repository or image in an Azure Container Registry.
    '''
    return call_az("az acr repository delete", locals())


def untag(image, name, password=None, resource_group=None, suffix=None, username=None, **kwargs):
    '''
    Untag an image in an Azure Container Registry.
    '''
    return call_az("az acr repository untag", locals())

