from ... pyaz_utils import call_az

def add(allowed_origins, name, resource_group, slot=None, **kwargs):
    '''
    Add allowed origins
    '''
    return call_az("az functionapp cors add", locals())


def remove(allowed_origins, name, resource_group, slot=None, **kwargs):
    '''
    Remove allowed origins
    '''
    return call_az("az functionapp cors remove", locals())


def show(name, resource_group, slot=None, **kwargs):
    '''
    show allowed origins
    '''
    return call_az("az functionapp cors show", locals())

