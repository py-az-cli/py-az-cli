from .... pyaz_utils import call_az

def show(account, pipeline_identity, end_date_time=None, start_date_time=None, **kwargs):
    '''
    Retrieve a job pipeline in a Data Lake Analytics account.
    '''
    return call_az("az dla job pipeline show", locals())


def list(account, end_date_time=None, start_date_time=None, **kwargs):
    '''
    List job pipelines in a Data Lake Analytics account.
    '''
    return call_az("az dla job pipeline list", locals())

