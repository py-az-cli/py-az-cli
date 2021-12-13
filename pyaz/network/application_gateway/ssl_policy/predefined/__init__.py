from ..... pyaz_utils import call_az

def list(**kwargs):
    '''
    Lists all SSL predefined policies for configuring SSL policy.
    '''
    return call_az("az network application-gateway ssl-policy predefined list", locals())


def show(name, **kwargs):
    '''
    Gets SSL predefined policy with the specified policy name.
    '''
    return call_az("az network application-gateway ssl-policy predefined show", locals())

