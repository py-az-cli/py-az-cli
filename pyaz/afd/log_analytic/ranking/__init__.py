from .... pyaz_utils import _call_az

def list(date_time_begin, date_time_end, max_ranking, metrics, profile_name, rankings, resource_group, custom_domains=None):
    return _call_az("az afd log-analytic ranking list", locals())

