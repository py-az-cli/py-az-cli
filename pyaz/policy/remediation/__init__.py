from ... pyaz_utils import call_az
from . import deployment


def show(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Show a resource policy remediation.
    '''
    return call_az("az policy remediation show", locals())


def list(management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    List resource policy remediations.
    '''
    return call_az("az policy remediation list", locals())


def delete(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Delete a resource policy remediation.
    '''
    return call_az("az policy remediation delete", locals())


def cancel(name, management_group=None, namespace=None, parent=None, resource=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Cancel a resource policy remediation.
    '''
    return call_az("az policy remediation cancel", locals())


def create(name, policy_assignment, definition_reference_id=None, location_filters=None, management_group=None, namespace=None, parent=None, resource=None, resource_discovery_mode=None, resource_group=None, resource_type=None, **kwargs):
    '''
    Create a resource policy remediation.
    '''
    return call_az("az policy remediation create", locals())

