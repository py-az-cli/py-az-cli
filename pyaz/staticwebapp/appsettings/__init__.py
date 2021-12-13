from ... pyaz_utils import call_az

def list(name, resource_group=None, **kwargs):
    '''
    List app settings of the static app.
    '''
    return call_az("az staticwebapp appsettings list", locals())


def set(name, setting_names, resource_group=None, **kwargs):
    '''
    Add to or change the app settings of the static app.
    '''
    return call_az("az staticwebapp appsettings set", locals())


def delete(name, setting_names, resource_group=None, **kwargs):
    '''
    Delete app settings with given keys of the static app.
    '''
    return call_az("az staticwebapp appsettings delete", locals())

