from .... pyaz_utils import call_az
from . import throughput


def create(account_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Create an Cassandra keyspace under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb cassandra keyspace create", locals())


def exists(account_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb cassandra keyspace exists", locals())


def list(account_name, resource_group, **kwargs):
    '''
    List the Cassandra keyspaces under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb cassandra keyspace list", locals())


def show(account_name, name, resource_group, **kwargs):
    '''
    Show the details of a Cassandra keyspace under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb cassandra keyspace show", locals())


def delete(account_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the Cassandra keyspace under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb cassandra keyspace delete", locals())

