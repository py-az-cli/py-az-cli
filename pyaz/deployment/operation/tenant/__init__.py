from .... pyaz_utils import call_az

def list(name, **kwargs):
    '''
    List deployment operations at tenant scope.
    '''
    return call_az("az deployment operation tenant list", locals())


def show(name, operation_ids, **kwargs):
    '''
    Show a deployment operation at tenant scope.
    '''
    return call_az("az deployment operation tenant show", locals())

