from ..... pyaz_utils import call_az

def add(name, resource_group, scope, reset=None, **kwargs):
    '''
    Add scopes to this activity log alert.
    '''
    return call_az("az monitor activity-log alert scope add", locals())


def remove(name, resource_group, scope, **kwargs):
    '''
    Removes scopes from this activity log alert.
    '''
    return call_az("az monitor activity-log alert scope remove", locals())

