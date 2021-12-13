from .... pyaz_utils import call_az

def show(account_name, name, resource_group, **kwargs):
    '''
    Get the throughput of the Table under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table throughput show", locals())


def update(account_name, name, resource_group, max_throughput=None, throughput=None, **kwargs):
    '''
    Update the throughput of the Table under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb table throughput update", locals())


def migrate(account_name, name, resource_group, throughput_type, **kwargs):
    '''
    Migrate the throughput of the Table between autoscale and manually provisioned.
    '''
    return call_az("az cosmosdb table throughput migrate", locals())

