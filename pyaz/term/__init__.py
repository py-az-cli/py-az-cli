from .. pyaz_utils import call_az

def show(plan, product, publisher, **kwargs):
    '''
    Get marketplace terms.
    '''
    return call_az("az term show", locals())


def accept(plan, product, publisher, **kwargs):
    '''
    Accept marketplace terms.
    '''
    return call_az("az term accept", locals())

