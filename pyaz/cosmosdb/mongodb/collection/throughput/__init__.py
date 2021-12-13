from ..... pyaz_utils import call_az

def show(account_name, database_name, name, resource_group, **kwargs):
    '''
    Get the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection throughput show", locals())


def update(account_name, database_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Update the throughput of the MongoDB collection under an Azure Cosmos DB MongoDB database.
    '''
    return call_az("az cosmosdb mongodb collection throughput update", locals())


def migrate(account_name, database_name, name, resource_group, throughput_type, **kwargs):
    '''
    Migrate the throughput of the MongoDB collection between autoscale and manually provisioned.
    '''
    return call_az("az cosmosdb mongodb collection throughput migrate", locals())

