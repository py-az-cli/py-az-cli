from .... pyaz_utils import _call_az

def list(resource_group, server_name):
    '''
    List all read replicas for a given server.
    '''
    return _call_az("az postgres server replica list", locals())


def create(name, resource_group, source_server, location=None, no_wait=None, sku_name=None):
    '''
    Create a read replica for a server.
    '''
    return _call_az("az postgres server replica create", locals())


def stop(name, resource_group, yes=None):
    '''
    Stop replication to a read replica and make it a read/write server.
    '''
    return _call_az("az postgres server replica stop", locals())

