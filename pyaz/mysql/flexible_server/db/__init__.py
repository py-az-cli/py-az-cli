from .... pyaz_utils import call_az

def create(resource_group, server_name, charset=None, collation=None, database_name=None, **kwargs):
    '''
    Create a MySQL database on a flexible server.
    '''
    return call_az("az mysql flexible-server db create", locals())


def delete(database_name=None, resource_group=None, server_name=None, yes=None, **kwargs):
    '''
    Delete a database on a flexible server.
    '''
    return call_az("az mysql flexible-server db delete", locals())


def show(database_name, resource_group, server_name, **kwargs):
    '''
    Show the details of a database.
    '''
    return call_az("az mysql flexible-server db show", locals())


def list(resource_group, server_name, **kwargs):
    '''
    List the databases for a flexible server.
    '''
    return call_az("az mysql flexible-server db list", locals())

