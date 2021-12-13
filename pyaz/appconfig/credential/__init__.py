from ... pyaz_utils import call_az

def list(name, resource_group=None, **kwargs):
    '''
    List access keys of an App Configuration.
    '''
    return call_az("az appconfig credential list", locals())


def regenerate(id, name, resource_group=None, **kwargs):
    '''
    Regenerate an access key for an App Configuration.
    '''
    return call_az("az appconfig credential regenerate", locals())

