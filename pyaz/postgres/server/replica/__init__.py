from .... pyaz_utils import call_az

def list(resource_group, server_name, **kwargs):
    '''
    List all read replicas for a given server.
    '''
    return call_az("az postgres server replica list", locals())


def create(name, resource_group, source_server, location=None, no_wait=None, sku_name=None, **kwargs):
    '''
    Create a read replica for a server.
    '''
    return call_az("az postgres server replica create", locals())


def stop(name, resource_group, yes=None, **kwargs):
    '''
    Stop replication to a read replica and make it a read/write server.
    '''
    return call_az("az postgres server replica stop", locals())

