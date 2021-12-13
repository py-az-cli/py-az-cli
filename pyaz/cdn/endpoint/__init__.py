from ... pyaz_utils import call_az
from . import rule


def start(name, profile_name, resource_group, no_wait=None, **kwargs):
    '''
    Start a CDN endpoint.
    '''
    return call_az("az cdn endpoint start", locals())


def stop(name, profile_name, resource_group, no_wait=None, **kwargs):
    '''
    Stop a CDN endpoint.
    '''
    return call_az("az cdn endpoint stop", locals())


def delete(name, profile_name, resource_group, no_wait=None, **kwargs):
    '''
    Delete a CDN endpoint.
    '''
    return call_az("az cdn endpoint delete", locals())


def show(name, profile_name, resource_group, **kwargs):
    return call_az("az cdn endpoint show", locals())


def list(profile_name, resource_group, **kwargs):
    '''
    List available endpoints for a CDN.
    '''
    return call_az("az cdn endpoint list", locals())


def load(content_paths, name, profile_name, resource_group, no_wait=None, **kwargs):
    '''
    Pre-load content for a CDN endpoint.
    '''
    return call_az("az cdn endpoint load", locals())


def purge(content_paths, name, profile_name, resource_group, no_wait=None, **kwargs):
    '''
    Purge pre-loaded content for a CDN endpoint.
    '''
    return call_az("az cdn endpoint purge", locals())


def validate_custom_domain(host_name, name, profile_name, resource_group, **kwargs):
    '''
    Validates the custom domain mapping to ensure it maps to the correct CDN endpoint in DNS.
    '''
    return call_az("az cdn endpoint validate-custom-domain", locals())


def create(name, origin, profile_name, resource_group, content_types_to_compress=None, enable_compression=None, location=None, no_http=None, no_https=None, no_wait=None, origin_host_header=None, origin_path=None, query_string_caching_behavior=None, tags=None, **kwargs):
    '''
    Create a named endpoint to connect to a CDN.
    '''
    return call_az("az cdn endpoint create", locals())


def update(name, profile_name, resource_group, add=None, content_types_to_compress=None, default_origin_group=None, enable_compression=None, force_string=None, no_http=None, no_https=None, no_wait=None, origin_host_header=None, origin_path=None, query_string_caching=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update a CDN endpoint to manage how content is delivered.
    '''
    return call_az("az cdn endpoint update", locals())

