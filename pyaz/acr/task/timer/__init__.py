from .... pyaz_utils import call_az

def add(name, registry, schedule, timer_name, enabled=None, resource_group=None, **kwargs):
    '''
    Add a timer trigger to a task.
    '''
    return call_az("az acr task timer add", locals())


def update(name, registry, timer_name, enabled=None, resource_group=None, schedule=None, **kwargs):
    '''
    Update the timer trigger for a task.
    '''
    return call_az("az acr task timer update", locals())


def remove(name, registry, timer_name, resource_group=None, **kwargs):
    '''
    Remove a timer trigger from a task.
    '''
    return call_az("az acr task timer remove", locals())


def list(name, registry, resource_group=None, **kwargs):
    '''
    List all timer triggers for a task.
    '''
    return call_az("az acr task timer list", locals())

