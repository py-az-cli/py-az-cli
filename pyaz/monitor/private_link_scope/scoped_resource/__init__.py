from .... pyaz_utils import call_az

def show(name, resource_group, scope_name, **kwargs):
    '''
    Show a scoped resource of a private link scope resource.
    '''
    return call_az("az monitor private-link-scope scoped-resource show", locals())


def list(resource_group, scope_name, **kwargs):
    '''
    List all scoped resource of a private link scope resource.
    '''
    return call_az("az monitor private-link-scope scoped-resource list", locals())


def create(linked_resource, name, resource_group, scope_name, **kwargs):
    '''
    Create a scoped resource for a private link scope resource.
    '''
    return call_az("az monitor private-link-scope scoped-resource create", locals())


def delete(name, resource_group, scope_name, yes=None, **kwargs):
    '''
    Delete a scoped resource of a private link scope resource.
    '''
    return call_az("az monitor private-link-scope scoped-resource delete", locals())

