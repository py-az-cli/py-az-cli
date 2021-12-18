from ... pyaz_utils import _call_az

def list():
    '''
    List of secure-scores details and state results.
    '''
    return _call_az("az security secure-scores list", locals())


def show(name):
    '''
    Shows a secure score details for selected initiative.
    '''
    return _call_az("az security secure-scores show", locals())

