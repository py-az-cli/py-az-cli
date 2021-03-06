'''
Shows the Azure Security Center Home region location.
'''
from ... pyaz_utils import _call_az

def list():
    '''
    Shows the Azure Security Center Home region location.
    '''
    return _call_az("az security location list", locals())


def show(name):
    '''
    Shows the Azure Security Center Home region location.

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security location show", locals())

