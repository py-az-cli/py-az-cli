from .... pyaz_utils import call_az

def sync(name, resource_group, **kwargs):
    return call_az("az batch account autostorage-keys sync", locals())

