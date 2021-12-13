from .... pyaz_utils import call_az

def list(name, resource_group, **kwargs):
    '''
    List all deployment slots.
    '''
    return call_az("az functionapp deployment slot list", locals())


def delete(name, resource_group, slot, **kwargs):
    '''
    Delete a deployment slot.
    '''
    return call_az("az functionapp deployment slot delete", locals())


def auto_swap(name, resource_group, slot, auto_swap_slot=None, disable=None, **kwargs):
    '''
    Configure deployment slot auto swap.
    '''
    return call_az("az functionapp deployment slot auto-swap", locals())


def swap(name, resource_group, slot, action=None, preserve_vnet=None, target_slot=None, **kwargs):
    '''
    Swap deployment slots for a function app.
    '''
    return call_az("az functionapp deployment slot swap", locals())


def create(name, resource_group, slot, configuration_source=None, **kwargs):
    '''
    Create a deployment slot.
    '''
    return call_az("az functionapp deployment slot create", locals())

