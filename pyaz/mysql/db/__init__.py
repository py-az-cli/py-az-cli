from ... pyaz_utils import call_az

def create(name, resource_group, server_name, charset=None, collation=None, **kwargs):
    '''
    Create a MySQL database.
    '''
    return call_az("az mysql db create", locals())


def delete(name, resource_group, server_name, yes=None, **kwargs):
    '''
    Delete a database.
    '''
    return call_az("az mysql db delete", locals())


def show(name, resource_group, server_name, **kwargs):
    '''
    Show the details of a database.
    '''
    return call_az("az mysql db show", locals())


def list(resource_group, server_name, **kwargs):
    '''
    List the databases for a server.
    '''
    return call_az("az mysql db list", locals())

