from .... pyaz_utils import call_az
from . import throughput


def create(account_name, keyspace_name, name, resource_group, schema, analytical_storage_ttl=None, max_throughput=None, throughput=None, ttl=None, **kwargs):
    '''
    Create an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
    '''
    return call_az("az cosmosdb cassandra table create", locals())


def update(account_name, keyspace_name, name, resource_group, analytical_storage_ttl=None, schema=None, ttl=None, **kwargs):
    '''
    Update an Cassandra table under an Azure Cosmos DB Cassandra keyspace.
    '''
    return call_az("az cosmosdb cassandra table update", locals())


def exists(account_name, keyspace_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb cassandra table exists", locals())


def list(account_name, keyspace_name, resource_group, **kwargs):
    '''
    List the Cassandra tables under an Azure Cosmos DB Cassandra keyspace.
    '''
    return call_az("az cosmosdb cassandra table list", locals())


def show(account_name, keyspace_name, name, resource_group, **kwargs):
    '''
    Show the details of a Cassandra table under an Azure Cosmos DB Cassandra keyspace.
    '''
    return call_az("az cosmosdb cassandra table show", locals())


def delete(account_name, keyspace_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the Cassandra table under an Azure Cosmos DB Cassandra keyspace.
    '''
    return call_az("az cosmosdb cassandra table delete", locals())

