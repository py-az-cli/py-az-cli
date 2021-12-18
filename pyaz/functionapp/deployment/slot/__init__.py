from .... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List all deployment slots.
    '''
    return _call_az("az functionapp deployment slot list", locals())


def delete(name, resource_group, slot):
    '''
    Delete a deployment slot.
    '''
    return _call_az("az functionapp deployment slot delete", locals())


def auto_swap(name, resource_group, slot, auto_swap_slot=None, disable=None):
    '''
    Configure deployment slot auto swap.
    '''
    return _call_az("az functionapp deployment slot auto-swap", locals())


def swap(name, resource_group, slot, action=None, preserve_vnet=None, target_slot=None):
    '''
    Swap deployment slots for a function app.
    '''
    return _call_az("az functionapp deployment slot swap", locals())


def create(name, resource_group, slot, configuration_source=None):
    '''
    Create a deployment slot.
    '''
    return _call_az("az functionapp deployment slot create", locals())

