from ... pyaz_utils import call_az

def on(**kwargs):
    '''
    Turn on parameter persistence.
    '''
    return call_az("az config param-persist on", locals())


def off(**kwargs):
    '''
    Turn off parameter persistence.
    '''
    return call_az("az config param-persist off", locals())


def show(**kwargs):
    '''
    Show parameter persistence data.
    '''
    return call_az("az config param-persist show", locals())


def delete(all=None, purge=None, recursive=None, yes=None, **kwargs):
    '''
    Delete parameter persistence data.
    '''
    return call_az("az config param-persist delete", locals())

