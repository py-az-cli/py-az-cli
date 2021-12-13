from ... pyaz_utils import call_az

def list(resource_group=None, **kwargs):
    '''
    List security tasks (recommendations).
    '''
    return call_az("az security task list", locals())


def show(name, resource_group=None, **kwargs):
    '''
    shows a security task (recommendation).
    '''
    return call_az("az security task show", locals())

