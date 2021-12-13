from ... pyaz_utils import call_az

def list(registry, resource_group=None, **kwargs):
    '''
    List the taskruns for an Azure Container Registry.
    '''
    return call_az("az acr taskrun list", locals())


def delete(name, registry, resource_group=None, yes=None, **kwargs):
    '''
    Delete a taskrun from an Azure Container Registry.
    '''
    return call_az("az acr taskrun delete", locals())


def show(name, registry, resource_group=None, **kwargs):
    '''
    Get the properties of a named taskrun for an Azure Container Registry.
    '''
    return call_az("az acr taskrun show", locals())


def logs(name, registry, resource_group=None, **kwargs):
    '''
    Show run logs for a particular taskrun.
    '''
    return call_az("az acr taskrun logs", locals())

