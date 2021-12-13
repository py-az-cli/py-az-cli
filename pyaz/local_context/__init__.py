from .. pyaz_utils import call_az

def on(**kwargs):
    '''
    Turn on local context
    '''
    return call_az("az local-context on", locals())


def off(**kwargs):
    '''
    Turn off local context
    '''
    return call_az("az local-context off", locals())


def show(name=None, **kwargs):
    '''
    Show local context data
    '''
    return call_az("az local-context show", locals())


def delete(all=None, name=None, purge=None, recursive=None, yes=None, **kwargs):
    '''
    Delete local context data
    '''
    return call_az("az local-context delete", locals())

