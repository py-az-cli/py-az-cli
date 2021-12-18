from .... pyaz_utils import _call_az

def update(name, registry, add=None, remove=None, resource_group=None):
    '''
    Add and remove repository permissions accross all the necessary connected registry sync scope maps.
    '''
    return _call_az("az acr connected-registry permissions update", locals())


def show(name, registry, resource_group=None):
    '''
    Show the connected registry sync scope map information.
    '''
    return _call_az("az acr connected-registry permissions show", locals())

