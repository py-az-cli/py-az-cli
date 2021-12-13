from ... pyaz_utils import call_az

def list(resource_group, service_name, **kwargs):
    return call_az("az search query-key list", locals())


def create(name, resource_group, service_name, **kwargs):
    return call_az("az search query-key create", locals())


def delete(key_value, resource_group, service_name, **kwargs):
    return call_az("az search query-key delete", locals())

