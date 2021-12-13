from .... pyaz_utils import call_az

def show(account, database_name, procedure_name, schema_name, **kwargs):
    return call_az("az dla catalog procedure show", locals())


def list(account, database_name, schema_name, count=None, filter=None, orderby=None, select=None, skip=None, top=None, **kwargs):
    return call_az("az dla catalog procedure list", locals())

