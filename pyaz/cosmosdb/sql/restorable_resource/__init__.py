from .... pyaz_utils import call_az

def list(instance_id, location, restore_location, restore_timestamp, **kwargs):
    '''
    List all the databases and its containers that can be restored in the given account at the given timesamp and region.
    '''
    return call_az("az cosmosdb sql restorable-resource list", locals())

