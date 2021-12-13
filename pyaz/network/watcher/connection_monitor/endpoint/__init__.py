from ..... pyaz_utils import call_az

def add(connection_monitor, location, name, address=None, address_exclude=None, address_include=None, coverage_level=None, dest_test_groups=None, filter_item=None, filter_type=None, resource_id=None, source_test_groups=None, type=None, **kwargs):
    '''
    Add an endpoint to a connection monitor
    '''
    return call_az("az network watcher connection-monitor endpoint add", locals())


def remove(connection_monitor, location, name, test_groups=None, **kwargs):
    '''
    Remove an endpoint from a connection monitor
    '''
    return call_az("az network watcher connection-monitor endpoint remove", locals())


def show(connection_monitor, location, name, **kwargs):
    '''
    Show an endpoint from a connection monitor
    '''
    return call_az("az network watcher connection-monitor endpoint show", locals())


def list(connection_monitor, location, **kwargs):
    '''
    List all endpoints form a connection monitor
    '''
    return call_az("az network watcher connection-monitor endpoint list", locals())

