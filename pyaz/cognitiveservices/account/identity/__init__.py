'''
Manage identity of Cognitive Services accounts.
'''
from .... pyaz_utils import _call_az

def assign(name, resource_group):
    '''
    Assign an identity of a Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account identity assign", locals())


def remove(name, resource_group):
    '''
    Remove the identity from a Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account identity remove", locals())


def show(name, resource_group):
    '''
    Show the identity of a Cognitive Services account.

    Required Parameters:
    - name -- cognitive service account name
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az cognitiveservices account identity show", locals())

