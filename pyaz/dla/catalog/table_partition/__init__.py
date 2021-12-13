from .... pyaz_utils import call_az

def show(account, database_name, partition_name, schema_name, table_name, **kwargs):
    return call_az("az dla catalog table-partition show", locals())


def list(account, database_name, schema_name, table_name, count=None, filter=None, orderby=None, select=None, skip=None, top=None, **kwargs):
    return call_az("az dla catalog table-partition list", locals())

