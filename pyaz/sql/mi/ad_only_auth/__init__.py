from .... pyaz_utils import call_az

def disable(name, resource_group):
    '''
    Disable Azure Active Directly only Authentication for this Managed Instance.
    '''
    return call_az("az sql mi ad-only-auth disable", locals())


def enable(name, resource_group):
    '''
    Enable Azure Active Directly only Authentication for this Managed Instance.
    '''
    return call_az("az sql mi ad-only-auth enable", locals())


def get(name, resource_group):
    '''
    Get a specific Azure Active Directly only Authentication property.
    '''
    return call_az("az sql mi ad-only-auth get", locals())
