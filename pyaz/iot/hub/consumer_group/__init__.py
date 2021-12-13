from .... pyaz_utils import call_az

def create(hub_name, name, event_hub_name=None, resource_group=None, **kwargs):
    '''
    Create an event hub consumer group.
    '''
    return call_az("az iot hub consumer-group create", locals())


def list(hub_name, event_hub_name=None, resource_group=None, **kwargs):
    '''
    List event hub consumer groups.
    '''
    return call_az("az iot hub consumer-group list", locals())


def show(hub_name, name, event_hub_name=None, resource_group=None, **kwargs):
    '''
    Get the details for an event hub consumer group.
    '''
    return call_az("az iot hub consumer-group show", locals())


def delete(hub_name, name, event_hub_name=None, resource_group=None, **kwargs):
    '''
    Delete an event hub consumer group.
    '''
    return call_az("az iot hub consumer-group delete", locals())

