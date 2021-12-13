from .... pyaz_utils import call_az

def create(circuit_name, name, resource_group, **kwargs):
    '''
    Create a new link authorization for an ExpressRoute circuit.
    '''
    return call_az("az network express-route auth create", locals())


def delete(circuit_name, name, resource_group, **kwargs):
    '''
    Delete a link authorization of an ExpressRoute circuit.
    '''
    return call_az("az network express-route auth delete", locals())


def show(circuit_name, name, resource_group, **kwargs):
    '''
    Get the details of a link authorization of an ExpressRoute circuit.
    '''
    return call_az("az network express-route auth show", locals())


def list(circuit_name, resource_group, **kwargs):
    '''
    List link authorizations of an ExpressRoute circuit.
    '''
    return call_az("az network express-route auth list", locals())

