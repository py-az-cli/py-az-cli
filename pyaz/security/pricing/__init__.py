from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    Shows the Azure Defender plans for the subscription.
    '''
    return call_az("az security pricing list", locals())


def show(name, **kwargs):
    '''
    Shows the Azure Defender plan for the subscription
    '''
    return call_az("az security pricing show", locals())


def create(name, tier, **kwargs):
    '''
    Updates the Azure defender plan for the subscription.
    '''
    return call_az("az security pricing create", locals())

