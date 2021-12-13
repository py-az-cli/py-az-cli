from ... pyaz_utils import call_az

def show(instance_id=None, location=None, **kwargs):
    '''
    Show the details of a database account that can be restored.
    '''
    return call_az("az cosmosdb restorable-database-account show", locals())


def list(account_name=None, location=None, **kwargs):
    '''
    List all the database accounts that can be restored.
    '''
    return call_az("az cosmosdb restorable-database-account list", locals())

