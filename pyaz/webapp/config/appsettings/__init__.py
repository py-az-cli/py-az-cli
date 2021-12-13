from .... pyaz_utils import call_az

def list(name, resource_group, slot=None, **kwargs):
    '''
    Get the details of a web app's settings.
    '''
    return call_az("az webapp config appsettings list", locals())


def set(name, resource_group, settings=None, slot=None, slot_settings=None, **kwargs):
    '''
    Set a web app's settings.
    '''
    return call_az("az webapp config appsettings set", locals())


def delete(name, resource_group, setting_names, slot=None, **kwargs):
    '''
    Delete web app settings.
    '''
    return call_az("az webapp config appsettings delete", locals())

