from ... pyaz_utils import call_az

def list(namespace=None, **kwargs):
    '''
    List feature registrations.
    '''
    return call_az("az feature registration list", locals())


def show(name, provider_namespace, **kwargs):
    return call_az("az feature registration show", locals())


def create(name, namespace, **kwargs):
    '''
    Create a feature registration.
    '''
    return call_az("az feature registration create", locals())


def delete(name, namespace, yes=None, **kwargs):
    '''
    Delete a feature registration.
    '''
    return call_az("az feature registration delete", locals())

