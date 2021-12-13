from .... pyaz_utils import call_az

def list(name, resource_group, slot=None, **kwargs):
    '''
    List all triggered webjobs hosted on a web app.
    '''
    return call_az("az webapp webjob triggered list", locals())


def remove(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Delete a specific triggered webjob hosted on a web app.
    '''
    return call_az("az webapp webjob triggered remove", locals())


def run(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Run a specific triggered webjob hosted on a web app.
    '''
    return call_az("az webapp webjob triggered run", locals())


def log(name, resource_group, webjob_name, slot=None, **kwargs):
    '''
    Get history of a specific triggered webjob hosted on a web app.
    '''
    return call_az("az webapp webjob triggered log", locals())

