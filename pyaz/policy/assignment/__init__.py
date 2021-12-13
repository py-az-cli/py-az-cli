from ... pyaz_utils import call_az
from . import identity, non_compliance_message


def create(assign_identity=None, description=None, display_name=None, enforcement_mode=None, identity_scope=None, location=None, mi_system_assigned=None, mi_user_assigned=None, name=None, not_scopes=None, params=None, policy=None, policy_set_definition=None, resource_group=None, role=None, scope=None, sku=None, **kwargs):
    '''
    Create a resource policy assignment.
    '''
    return call_az("az policy assignment create", locals())


def delete(name, resource_group=None, scope=None, **kwargs):
    '''
    Delete a resource policy assignment.
    '''
    return call_az("az policy assignment delete", locals())


def list(disable_scope_strict_match=None, resource_group=None, scope=None, **kwargs):
    '''
    List resource policy assignments.
    '''
    return call_az("az policy assignment list", locals())


def show(name, resource_group=None, scope=None, **kwargs):
    '''
    Show a resource policy assignment.
    '''
    return call_az("az policy assignment show", locals())


def update(description=None, display_name=None, enforcement_mode=None, name=None, not_scopes=None, params=None, resource_group=None, scope=None, sku=None, **kwargs):
    '''
    Update a resource policy assignment.
    '''
    return call_az("az policy assignment update", locals())

