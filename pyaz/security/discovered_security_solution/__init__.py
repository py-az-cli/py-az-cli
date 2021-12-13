from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    List the discovered security solutions.
    '''
    return call_az("az security discovered-security-solution list", locals())


def show(name, resource_group, **kwargs):
    '''
    Shows a discovered security solution.
    '''
    return call_az("az security discovered-security-solution show", locals())

