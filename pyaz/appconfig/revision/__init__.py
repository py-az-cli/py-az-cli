from ... pyaz_utils import _call_az

def list(all=None, auth_mode=None, connection_string=None, datetime=None, endpoint=None, fields=None, key=None, label=None, name=None, top=None):
    '''
    Lists revision history of key-values.
    '''
    return _call_az("az appconfig revision list", locals())

