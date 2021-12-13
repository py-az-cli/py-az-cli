from .... pyaz_utils import call_az

def list(name, **kwargs):
    '''
    List deployment operations at subscription scope.
    '''
    return call_az("az deployment operation sub list", locals())


def show(name, operation_ids, **kwargs):
    '''
    Show a deployment operation at subscription scope.
    '''
    return call_az("az deployment operation sub show", locals())

