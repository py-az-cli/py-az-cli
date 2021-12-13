from .... pyaz_utils import call_az

def show(database, location, name, server, **kwargs):
    '''
    Get a long term retention backup for a database.
    '''
    return call_az("az sql db ltr-backup show", locals())


def list(location, database=None, database_state=None, only_latest_per_database=None, resource_group=None, server=None, **kwargs):
    '''
    List the long term retention backups for a location, server or database.
    '''
    return call_az("az sql db ltr-backup list", locals())


def delete(database, location, name, server, yes=None, **kwargs):
    '''
    Delete a long term retention backup.
    '''
    return call_az("az sql db ltr-backup delete", locals())


def restore(backup_id, dest_database, dest_resource_group, dest_server, backup_storage_redundancy=None, no_wait=None, **kwargs):
    '''
    Restore a long term retention backup to a new database.
    '''
    return call_az("az sql db ltr-backup restore", locals())


def wait(name, resource_group, server, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the database is met.
    '''
    return call_az("az sql db ltr-backup wait", locals())

