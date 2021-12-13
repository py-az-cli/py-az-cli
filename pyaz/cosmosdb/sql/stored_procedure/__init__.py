from .... pyaz_utils import call_az

def create(account_name, body, container_name, database_name, name, resource_group, **kwargs):
    '''
    Create an SQL stored procedure under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql stored-procedure create", locals())


def update(account_name, body, container_name, database_name, name, resource_group, **kwargs):
    return call_az("az cosmosdb sql stored-procedure update", locals())


def list(account_name, container_name, database_name, resource_group, **kwargs):
    '''
    List the SQL stored procedures under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql stored-procedure list", locals())


def show(account_name, container_name, database_name, name, resource_group, **kwargs):
    '''
    Show the details of a SQL stored procedure under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql stored-procedure show", locals())


def delete(account_name, container_name, database_name, name, resource_group, yes=None, **kwargs):
    '''
    Delete the SQL stored procedure under an Azure Cosmos DB SQL container.
    '''
    return call_az("az cosmosdb sql stored-procedure delete", locals())

