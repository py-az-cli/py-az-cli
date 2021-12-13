from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    List supported regulatory compliance standards details and state results.
    '''
    return call_az("az security regulatory-compliance-standards list", locals())


def show(name, **kwargs):
    '''
    Shows a regulatory compliance details state for selected standard.
    '''
    return call_az("az security regulatory-compliance-standards show", locals())

