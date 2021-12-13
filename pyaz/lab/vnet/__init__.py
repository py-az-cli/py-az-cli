from ... pyaz_utils import call_az

def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None, **kwargs):
    return call_az("az lab vnet list", locals())


def get(lab_name, name, resource_group, expand=None, **kwargs):
    return call_az("az lab vnet get", locals())

