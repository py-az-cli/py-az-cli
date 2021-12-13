from .... pyaz_utils import call_az

def list(profile_name, resource_group, **kwargs):
    return call_az("az afd log-analytic location list", locals())

