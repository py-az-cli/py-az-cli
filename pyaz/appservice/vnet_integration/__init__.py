from ... pyaz_utils import call_az

def list(plan, resource_group, **kwargs):
    '''
    list the virtual network integrations used in an appservice plan
    '''
    return call_az("az appservice vnet-integration list", locals())

