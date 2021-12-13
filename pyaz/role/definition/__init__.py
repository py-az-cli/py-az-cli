from ... pyaz_utils import call_az

def list(custom_role_only=None, name=None, resource_group=None, scope=None, **kwargs):
    '''
    List role definitions.
    '''
    return call_az("az role definition list", locals())


def delete(name, custom_role_only=None, resource_group=None, scope=None, **kwargs):
    '''
    Delete a role definition.
    '''
    return call_az("az role definition delete", locals())


def create(role_definition, **kwargs):
    '''
    Create a custom role definition.
    '''
    return call_az("az role definition create", locals())


def update(role_definition, **kwargs):
    '''
    Update a role definition.
    '''
    return call_az("az role definition update", locals())

