from .... pyaz_utils import _call_az

def show(account, database_name, schema_name, table_type_name):
    return _call_az("az dla catalog table-type show", locals())


def list(account, database_name, schema_name, count=None, filter=None, orderby=None, select=None, skip=None, top=None):
    return _call_az("az dla catalog table-type list", locals())

