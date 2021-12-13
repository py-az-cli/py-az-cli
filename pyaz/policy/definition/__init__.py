from ... pyaz_utils import call_az

def create(name, description=None, display_name=None, management_group=None, metadata=None, mode=None, params=None, rules=None, subscription=None, **kwargs):
    '''
    Create a policy definition.
    '''
    return call_az("az policy definition create", locals())


def delete(name, management_group=None, subscription=None, **kwargs):
    '''
    Delete a policy definition.
    '''
    return call_az("az policy definition delete", locals())


def list(management_group=None, subscription=None, **kwargs):
    '''
    List policy definitions.
    '''
    return call_az("az policy definition list", locals())


def show(name, management_group=None, subscription=None, **kwargs):
    '''
    Show a policy definition.
    '''
    return call_az("az policy definition show", locals())


def update(name, description=None, display_name=None, management_group=None, metadata=None, mode=None, params=None, rules=None, subscription=None, **kwargs):
    '''
    Update a policy definition.
    '''
    return call_az("az policy definition update", locals())

