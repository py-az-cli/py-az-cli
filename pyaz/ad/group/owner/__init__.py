from .... pyaz_utils import call_az

def list(group, **kwargs):
    '''
    List group owners.
    '''
    return call_az("az ad group owner list", locals())


def add(group, owner_object_id, **kwargs):
    '''
    Add a group owner.
    '''
    return call_az("az ad group owner add", locals())


def remove(group, owner_object_id, **kwargs):
    '''
    Remove a group owner.
    '''
    return call_az("az ad group owner remove", locals())

