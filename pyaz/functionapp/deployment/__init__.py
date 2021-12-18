from ... pyaz_utils import _call_az
from . import container, slot, source, user


def list_publishing_profiles(name, resource_group, slot=None, xml=None):
    '''
    Get the details for available function app deployment profiles.
    '''
    return _call_az("az functionapp deployment list-publishing-profiles", locals())


def list_publishing_credentials(name, resource_group, slot=None):
    '''
    Get the details for available function app publishing credentials.
    '''
    return _call_az("az functionapp deployment list-publishing-credentials", locals())

