from ... pyaz_utils import call_az

def list(resource_group, service_name, **kwargs):
    return call_az("az search private-link-resource list", locals())

