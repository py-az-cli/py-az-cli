from .... pyaz_utils import _call_az

def show(job_id, account_endpoint=None, account_key=None, account_name=None):
    return _call_az("az batch job task-counts show", locals())

