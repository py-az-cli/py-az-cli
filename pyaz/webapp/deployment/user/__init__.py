from .... pyaz_utils import call_az

def show(**kwargs):
    '''
    Get deployment publishing user.
    '''
    return call_az("az webapp deployment user show", locals())


def set(user_name, password=None, **kwargs):
    '''
    Update deployment credentials.
    '''
    return call_az("az webapp deployment user set", locals())

