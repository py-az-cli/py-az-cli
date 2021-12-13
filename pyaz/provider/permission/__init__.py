from ... pyaz_utils import call_az

def list(namespace, **kwargs):
    '''
    List permissions from a provider.
    '''
    return call_az("az provider permission list", locals())

