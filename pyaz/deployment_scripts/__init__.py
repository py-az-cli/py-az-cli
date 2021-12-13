from .. pyaz_utils import call_az

def list(resource_group=None, **kwargs):
    '''
    List all deployment scripts.
    '''
    return call_az("az deployment-scripts list", locals())


def show(name, resource_group, **kwargs):
    '''
    Retrieve a deployment script.
    '''
    return call_az("az deployment-scripts show", locals())


def show_log(name, resource_group, **kwargs):
    '''
    Show deployment script logs.
    '''
    return call_az("az deployment-scripts show-log", locals())


def delete(name, resource_group, yes=None, **kwargs):
    '''
    Delete a deployment script.
    '''
    return call_az("az deployment-scripts delete", locals())

