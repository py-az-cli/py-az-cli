from ..... pyaz_utils import call_az

def create(account_name, principal_id, resource_group, scope, no_wait=None, role_assignment_id=None, role_definition_id=None, role_definition_name=None, **kwargs):
    '''
    Create a SQL role assignment under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql role assignment create", locals())


def update(account_name, resource_group, role_assignment_id, no_wait=None, principal_id=None, role_definition_id=None, role_definition_name=None, scope=None, **kwargs):
    '''
    Update a SQL role assignment under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql role assignment update", locals())


def exists(account_name, resource_group, role_assignment_id, **kwargs):
    '''
    Check if an Azure Cosmos DB role assignment exists.
    '''
    return call_az("az cosmosdb sql role assignment exists", locals())


def list(account_name, resource_group, **kwargs):
    '''
    List all SQL role assignments under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql role assignment list", locals())


def show(account_name, resource_group, role_assignment_id, **kwargs):
    '''
    Show the properties of a SQL role assignment under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql role assignment show", locals())


def delete(account_name, resource_group, role_assignment_id, no_wait=None, yes=None, **kwargs):
    '''
    Delete a SQL role assignment under an Azure Cosmos DB account.
    '''
    return call_az("az cosmosdb sql role assignment delete", locals())


def wait(account_name, resource_group, role_assignment_id, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Poll on a SQL role assignment until a specific condition is met.
    '''
    return call_az("az cosmosdb sql role assignment wait", locals())

