from .... pyaz_utils import call_az

def show(resource_group, server, **kwargs):
    return call_az("az sql server tde-key show", locals())


def set(resource_group, server, server_key_type, auto_rotation_enabled=None, kid=None, **kwargs):
    '''
    Sets the server's encryption protector.
    '''
    return call_az("az sql server tde-key set", locals())

