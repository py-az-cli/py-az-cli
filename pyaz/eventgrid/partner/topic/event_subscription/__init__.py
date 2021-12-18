from ..... pyaz_utils import _call_az

def show(name, partner_topic_name, resource_group, include_full_endpoint_url=None, include_static_delivery_attribute_secret=None):
    '''
    Get the details of an event subscription of a partner topic.
    '''
    return _call_az("az eventgrid partner topic event-subscription show", locals())


def delete(name, partner_topic_name, resource_group, yes=None):
    '''
    Delete an event subscription of a partner topic
    '''
    return _call_az("az eventgrid partner topic event-subscription delete", locals())


def list(partner_topic_name, resource_group, odata_query=None):
    '''
    List event subscriptions of a specific partner topic.
    '''
    return _call_az("az eventgrid partner topic event-subscription list", locals())


def create(name, partner_topic_name, resource_group, advanced_filter=None, azure_active_directory_application_id_or_uri=None, azure_active_directory_tenant_id=None, deadletter_endpoint=None, delivery_attribute_mapping=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, event_delivery_schema=None, event_ttl=None, expiration_date=None, included_event_types=None, labels=None, max_delivery_attempts=None, max_events_per_batch=None, preferred_batch_size_in_kilobytes=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_case_sensitive=None, subject_ends_with=None):
    '''
    Create a new event subscription for a partner topic
    '''
    return _call_az("az eventgrid partner topic event-subscription create", locals())


def update(name, partner_topic_name, resource_group, advanced_filter=None, deadletter_endpoint=None, delivery_attribute_mapping=None, enable_advanced_filtering_on_arrays=None, endpoint=None, endpoint_type=None, included_event_types=None, labels=None, storage_queue_msg_ttl=None, subject_begins_with=None, subject_ends_with=None):
    '''
    Update an event subscription of a partner topic.
    '''
    return _call_az("az eventgrid partner topic event-subscription update", locals())

