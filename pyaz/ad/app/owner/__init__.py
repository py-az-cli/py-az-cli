from .... pyaz_utils import call_az

def list(id, **kwargs):
    '''
    List application owners.
    '''
    return call_az("az ad app owner list", locals())


def add(id, owner_object_id, **kwargs):
    '''
    Add an application owner.
    '''
    return call_az("az ad app owner add", locals())


def remove(id, owner_object_id, **kwargs):
    '''
    Remove an application owner.
    '''
    return call_az("az ad app owner remove", locals())

