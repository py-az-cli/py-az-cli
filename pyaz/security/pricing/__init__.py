'''
Enables managing the Azure Defender plan for the subscription
'''
from ... pyaz_utils import _call_az

def list():
    '''
    Shows the Azure Defender plans for the subscription.
    '''
    return _call_az("az security pricing list", locals())


def show(name):
    '''
    Shows the Azure Defender plan for the subscription

    Required Parameters:
    - name -- name of the resource to be fetched
    '''
    return _call_az("az security pricing show", locals())


def create(name, tier):
    '''
    Updates the Azure defender plan for the subscription.

    Required Parameters:
    - name -- name of the resource to be fetched
    - tier -- pricing tier type
    '''
    return _call_az("az security pricing create", locals())

