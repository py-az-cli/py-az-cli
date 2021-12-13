from ... pyaz_utils import call_az

def show(resource_group, service_name, **kwargs):
    return call_az("az search admin-key show", locals())


def renew(key_kind, resource_group, service_name, **kwargs):
    return call_az("az search admin-key renew", locals())

