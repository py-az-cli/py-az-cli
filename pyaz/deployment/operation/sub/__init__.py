'''
Manage deployment operations at subscription scope.
'''
from .... pyaz_utils import _call_az

def list(name):
    '''
    List deployment operations at subscription scope.

    Required Parameters:
    - name -- The deployment name.
    '''
    return _call_az("az deployment operation sub list", locals())


def show(name, operation_ids):
    '''
    Show a deployment operation at subscription scope.

    Required Parameters:
    - name -- The deployment name.
    - operation_ids -- A list of operation ids to show
    '''
    return _call_az("az deployment operation sub show", locals())

