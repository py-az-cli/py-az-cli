from ... pyaz_utils import call_az

def set(key, auth_mode=None, connection_string=None, content_type=None, endpoint=None, label=None, name=None, tags=None, value=None, yes=None, **kwargs):
    '''
    Set a key-value.
    '''
    return call_az("az appconfig kv set", locals())


def delete(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None, **kwargs):
    '''
    Delete key-values.
    '''
    return call_az("az appconfig kv delete", locals())


def show(key, auth_mode=None, connection_string=None, datetime=None, endpoint=None, label=None, name=None, **kwargs):
    '''
    Show all attributes of a key-value.
    '''
    return call_az("az appconfig kv show", locals())


def list(all=None, auth_mode=None, connection_string=None, datetime=None, endpoint=None, fields=None, key=None, label=None, name=None, resolve_keyvault=None, top=None, **kwargs):
    '''
    List key-values.
    '''
    return call_az("az appconfig kv list", locals())


def lock(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None, **kwargs):
    '''
    Lock a key-value to prohibit write operations.
    '''
    return call_az("az appconfig kv lock", locals())


def unlock(key, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, yes=None, **kwargs):
    '''
    Unlock a key-value to gain write operations.
    '''
    return call_az("az appconfig kv unlock", locals())


def restore(datetime, auth_mode=None, connection_string=None, endpoint=None, key=None, label=None, name=None, yes=None, **kwargs):
    '''
    Restore key-values.
    '''
    return call_az("az appconfig kv restore", locals())


def import_(source, appservice_account=None, auth_mode=None, connection_string=None, content_type=None, depth=None, endpoint=None, format=None, label=None, name=None, path=None, prefix=None, preserve_labels=None, profile=None, separator=None, skip_features=None, src_auth_mode=None, src_connection_string=None, src_endpoint=None, src_key=None, src_label=None, src_name=None, yes=None, **kwargs):
    '''
    Import configurations into your App Configuration from another place.
    '''
    return call_az("az appconfig kv import", locals())


def export(destination, appservice_account=None, auth_mode=None, connection_string=None, dest_auth_mode=None, dest_connection_string=None, dest_endpoint=None, dest_label=None, dest_name=None, endpoint=None, format=None, key=None, label=None, name=None, naming_convention=None, path=None, prefix=None, preserve_labels=None, profile=None, resolve_keyvault=None, separator=None, skip_features=None, skip_keyvault=None, yes=None, **kwargs):
    '''
    Export configurations to another place from your App Configuration.
    '''
    return call_az("az appconfig kv export", locals())


def set_keyvault(key, secret_identifier, auth_mode=None, connection_string=None, endpoint=None, label=None, name=None, tags=None, yes=None, **kwargs):
    '''
    Set a keyvault reference.
    '''
    return call_az("az appconfig kv set-keyvault", locals())

