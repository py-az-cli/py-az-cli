from .... pyaz_utils import call_az
from . import throughput


def create(account_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Create an MongoDB database under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb mongodb database create", locals())


def exists(account_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb mongodb database exists", locals())


def list(account_name, resource_group, **kwargs):
    '''
    List the MongoDB databases under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb mongodb database list", locals())


def show(account_name, name, resource_group, **kwargs):
    '''
    Show the details of a MongoDB database under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb mongodb database show", locals())


def delete(account_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the MongoDB database under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb mongodb database delete", locals())

