from .... pyaz_utils import call_az

def assign(name, resource_group, system_assigned=None, user_assigned=None, **kwargs):
    '''
    Assign Identities to Recovery Services vault.
    '''
    return call_az("az backup vault identity assign", locals())


def remove(name, resource_group, system_assigned=None, user_assigned=None, **kwargs):
    '''
    Remove Identities of Recovery Services vault.
    '''
    return call_az("az backup vault identity remove", locals())


def show(name, resource_group, **kwargs):
    '''
    Show Identities of Recovery Services vault.
    '''
    return call_az("az backup vault identity show", locals())

