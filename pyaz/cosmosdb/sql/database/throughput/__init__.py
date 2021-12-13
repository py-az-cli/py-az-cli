from ..... pyaz_utils import call_az

def show(account_name, name, resource_group, **kwargs):
    '''
    Get the throughput of the SQL database under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql database throughput show", locals())


def migrate(account_name, name, resource_group, throughput_type, **kwargs):
    '''
    Migrate the throughput of the SQL database between autoscale and manually provisioned.
    '''
    return call_az("az cosmosdb sql database throughput migrate", locals())


def update(account_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Update the throughput of the SQL database under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql database throughput update", locals())

