from .... pyaz_utils import _call_az

def list(instance_id, location):
    '''
    List all the versions of all the mongodb databases that were created / modified / deleted in the given restorable account.
    '''
    return _call_az("az cosmosdb mongodb restorable-database list", locals())

