from .... pyaz_utils import call_az
from . import throughput


def create(account_name, database_name, name, resource_group, analytical_storage_ttl=None, idx=None, max_throughput=None, shard=None, throughput=None, **kwargs):
    '''
    Create an MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection create", locals())


def update(account_name, database_name, name, resource_group, analytical_storage_ttl=None, idx=None, **kwargs):
    '''
    Update an MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection update", locals())


def exists(account_name, database_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb mongodb collection exists", locals())


def list(account_name, database_name, resource_group, **kwargs):
    '''
    List the MongoDB collections under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection list", locals())


def show(account_name, database_name, name, resource_group, **kwargs):
    '''
    Show the details of a MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection show", locals())


def delete(account_name, database_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection delete", locals())

