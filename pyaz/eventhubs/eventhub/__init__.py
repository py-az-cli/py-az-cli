from ... pyaz_utils import call_az
from . import authorization_rule, consumer_group


def create(name, namespace_name, resource_group, archive_name_format=None, blob_container=None, capture_interval=None, capture_size_limit=None, destination_name=None, enable_capture=None, message_retention=None, partition_count=None, skip_empty_archives=None, status=None, storage_account=None, **kwargs):
    '''
    Creates the EventHubs Eventhub
    '''
    return call_az("az eventhubs eventhub create", locals())


def show(name, namespace_name, resource_group, **kwargs):
    '''
    shows the Eventhub Details
    '''
    return call_az("az eventhubs eventhub show", locals())


def list(namespace_name, resource_group, skip=None, top=None, **kwargs):
    '''
    List the EventHub by Namespace
    '''
    return call_az("az eventhubs eventhub list", locals())


def delete(name, namespace_name, resource_group, **kwargs):
    '''
    Deletes the Eventhub
    '''
    return call_az("az eventhubs eventhub delete", locals())


def update(name, namespace_name, resource_group, add=None, archive_name_format=None, blob_container=None, capture_interval=None, capture_size_limit=None, destination_name=None, enable_capture=None, force_string=None, message_retention=None, partition_count=None, remove=None, set=None, skip_empty_archives=None, status=None, storage_account=None, **kwargs):
    '''
    Updates the EventHubs Eventhub
    '''
    return call_az("az eventhubs eventhub update", locals())

