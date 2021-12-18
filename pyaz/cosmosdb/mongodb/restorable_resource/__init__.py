from .... pyaz_utils import _call_az

def list(instance_id, location, restore_location, restore_timestamp):
    '''
    List all the databases and its collections that can be restored in the given account at the given timesamp and region.
    '''
    return _call_az("az cosmosdb mongodb restorable-resource list", locals())

