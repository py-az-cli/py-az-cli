from ... pyaz_utils import _call_az
from . import container, github_actions, slot, source, user


def list_publishing_profiles(name, resource_group, slot=None, xml=None):
    '''
    Get the details for available web app deployment profiles.
    '''
    return _call_az("az webapp deployment list-publishing-profiles", locals())


def list_publishing_credentials(name, resource_group, slot=None):
    '''
    Get the details for available web app publishing credentials
    '''
    return _call_az("az webapp deployment list-publishing-credentials", locals())

