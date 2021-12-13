from ..... pyaz_utils import call_az

def assign(identity, name, resource_group, no_wait=None, **kwargs):
    '''
    Assign a managed service identity to an ExpressRoute Port
    '''
    return call_az("az network express-route port identity assign", locals())


def remove(name, resource_group, no_wait=None, **kwargs):
    '''
    Remove the managed service identity of an ExpressRoute Port
    '''
    return call_az("az network express-route port identity remove", locals())


def show(name, resource_group, **kwargs):
    '''
    Show the managed service identity of an ExpressRoute Port
    '''
    return call_az("az network express-route port identity show", locals())

