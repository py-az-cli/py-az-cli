from ... pyaz_utils import call_az

def set(lab_name, name, resource_group, value, **kwargs):
    '''
    Set a secret for a lab.
    '''
    return call_az("az lab secret set", locals())


def show(lab_name, name, resource_group, expand=None, **kwargs):
    return call_az("az lab secret show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None, **kwargs):
    return call_az("az lab secret list", locals())


def delete(lab_name, name, resource_group, **kwargs):
    return call_az("az lab secret delete", locals())

