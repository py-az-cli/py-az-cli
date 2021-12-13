from ... pyaz_utils import call_az

def show(name, resource_group=None, **kwargs):
    '''
    Show the container registry's identity details
    '''
    return call_az("az acr identity show", locals())


def assign(identities, name, resource_group=None, **kwargs):
    '''
    Assign a managed identity to a container registry
    '''
    return call_az("az acr identity assign", locals())


def remove(identities, name, resource_group=None, **kwargs):
    '''
    Remove a managed identity from a container registry
    '''
    return call_az("az acr identity remove", locals())

