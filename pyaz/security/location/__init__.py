from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    Shows the Azure Security Center Home region location.
    '''
    return call_az("az security location list", locals())


def show(name, **kwargs):
    '''
    Shows the Azure Security Center Home region location.
    '''
    return call_az("az security location show", locals())

