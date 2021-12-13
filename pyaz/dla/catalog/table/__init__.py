from .... pyaz_utils import call_az

def show(account, database_name, schema_name, table_name, **kwargs):
    return call_az("az dla catalog table show", locals())


def list(account, database_name, schema_name=None, **kwargs):
    '''
    List tables in a database or schema.
    '''
    return call_az("az dla catalog table list", locals())

