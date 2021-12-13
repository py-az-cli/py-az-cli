from ... pyaz_utils import call_az

def assign(name, resource_group, identities=None, role=None, scope=None, **kwargs):
    '''
    Enable managed service identity on a VM.
    '''
    return call_az("az vm identity assign", locals())


def remove(name, resource_group, identities=None, **kwargs):
    '''
    Remove managed service identities from a VM.
    '''
    return call_az("az vm identity remove", locals())


def show(name, resource_group, **kwargs):
    '''
    display VM's managed identity info.
    '''
    return call_az("az vm identity show", locals())

