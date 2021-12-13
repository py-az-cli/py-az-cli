from ... pyaz_utils import call_az

def start(name, post_migration_name, resource_group, target_namespace, **kwargs):
    '''
    Create and Start Service Bus Migration of Standard to Premium namespace.
    '''
    return call_az("az servicebus migration start", locals())


def show(name, resource_group, **kwargs):
    '''
    shows properties of properties of Service Bus Migration
    '''
    return call_az("az servicebus migration show", locals())


def complete(name, resource_group, **kwargs):
    '''
    Completes the Service Bus Migration of Standard to Premium namespace
    '''
    return call_az("az servicebus migration complete", locals())


def abort(name, resource_group, **kwargs):
    '''
    Disable the Service Bus Migration of Standard to Premium namespace
    '''
    return call_az("az servicebus migration abort", locals())

