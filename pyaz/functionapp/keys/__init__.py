from ... pyaz_utils import call_az

def set(key_name, key_type, name, resource_group, key_value=None, slot=None, **kwargs):
    '''
    Create or update a function app key.
    '''
    return call_az("az functionapp keys set", locals())


def list(name, resource_group, slot=None, **kwargs):
    '''
    List all function app keys.
    '''
    return call_az("az functionapp keys list", locals())


def delete(key_name, key_type, name, resource_group, slot=None, **kwargs):
    '''
    Delete a function app key.
    '''
    return call_az("az functionapp keys delete", locals())

