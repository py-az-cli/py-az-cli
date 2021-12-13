from .... pyaz_utils import call_az

def list(name, resource_group, slot=None, **kwargs):
    '''
    List all continuous webjobs on a selected web app.
    '''
    return call_az("az webapp webjob continuous list", locals())


def remove(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Delete a specific continuous webjob.
    '''
    return call_az("az webapp webjob continuous remove", locals())


def start(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Start a specific continuous webjob on a selected web app.
    '''
    return call_az("az webapp webjob continuous start", locals())


def stop(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Stop a specific continuous webjob.
    '''
    return call_az("az webapp webjob continuous stop", locals())

