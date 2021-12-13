from .... pyaz_utils import call_az

def create(account_name, body, container_name, database_name, name, resource_group, operation=None, type=None, **kwargs):
    '''
    Create an SQL trigger under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql trigger create", locals())


def update(account_name, container_name, database_name, name, resource_group, body=None, operation=None, type=None, **kwargs):
    return call_az("az cosmosdb sql trigger update", locals())


def list(account_name, container_name, database_name, resource_group, **kwargs):
    '''
    List the SQL triggers under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql trigger list", locals())


def show(account_name, container_name, database_name, name, resource_group, **kwargs):
    '''
    Show the details of a SQL trigger under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql trigger show", locals())


def delete(account_name, container_name, database_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the SQL trigger under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql trigger delete", locals())

