from ... pyaz_utils import call_az
from . import throughput


def create(account_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Create an Table under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table create", locals())


def exists(account_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb table exists", locals())


def list(account_name, resource_group, **kwargs):
    '''
    List the Tables under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table list", locals())


def show(account_name, name, resource_group, **kwargs):
    '''
    Show the details of a Table under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table show", locals())


def delete(account_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the Table under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table delete", locals())

