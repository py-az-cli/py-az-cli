from .... pyaz_utils import call_az
from . import throughput


def create(account_name, database_name, name, partition_key_path, resource_group, conflict_resolution_policy=None, idx=None, max_throughput=None, throughput=None, ttl=None, **kwargs):
    '''
    Create an Gremlin graph under an Azure Cosmos DB Gremlin database.
    '''
    return call_az("az cosmosdb gremlin graph create", locals())


def update(account_name, database_name, name, resource_group, idx=None, ttl=None, **kwargs):
    '''
    Update an Gremlin graph under an Azure Cosmos DB Gremlin database.
    '''
    return call_az("az cosmosdb gremlin graph update", locals())


def exists(account_name, database_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb gremlin graph exists", locals())


def list(account_name, database_name, resource_group, **kwargs):
    '''
    List the Gremlin graphs under an Azure Cosmos DB Gremlin database.
    '''
    return call_az("az cosmosdb gremlin graph list", locals())


def show(account_name, database_name, name, resource_group, **kwargs):
    '''
    Show the details of a Gremlin graph under an Azure Cosmos DB Gremlin database.
    '''
    return call_az("az cosmosdb gremlin graph show", locals())


def delete(account_name, database_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the Gremlin graph under an Azure Cosmos DB Gremlin database.
    '''
    return call_az("az cosmosdb gremlin graph delete", locals())

