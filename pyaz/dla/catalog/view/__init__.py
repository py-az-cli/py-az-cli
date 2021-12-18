from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, view_name):
    return _call_az("az dla catalog view show", locals())


def list(account, database_name, schema_name=None):
    '''
    List views in a database or schema.
    '''
    return _call_az("az dla catalog view list", locals())

