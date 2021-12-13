from .... pyaz_utils import call_az

def create(eventhub_name, name, namespace_name, resource_group, user_metadata=None, **kwargs):
    '''
    Creates the EventHub ConsumerGroup
    '''
    return call_az("az eventhubs eventhub consumer-group create", locals())


def show(eventhub_name, name, namespace_name, resource_group, **kwargs):
    '''
    Shows the ConsumerGroup Details
    '''
    return call_az("az eventhubs eventhub consumer-group show", locals())


def list(eventhub_name, namespace_name, resource_group, skip=None, top=None, **kwargs):
    '''
    List the ConsumerGroup by Eventhub
    '''
    return call_az("az eventhubs eventhub consumer-group list", locals())


def delete(eventhub_name, name, namespace_name, resource_group, **kwargs):
    '''
    Deletes the ConsumerGroup
    '''
    return call_az("az eventhubs eventhub consumer-group delete", locals())


def update(eventhub_name, name, namespace_name, resource_group, add=None, force_string=None, remove=None, set=None, user_metadata=None, **kwargs):
    '''
    Updates the EventHub ConsumerGroup
    '''
    return call_az("az eventhubs eventhub consumer-group update", locals())

