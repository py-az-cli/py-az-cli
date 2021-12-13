from .... pyaz_utils import call_az

def show(account, recurrence_identity, end_date_time=None, start_date_time=None, **kwargs):
    '''
    Retrieve a job recurrence in a Data Lake Analytics account.
    '''
    return call_az("az dla job recurrence show", locals())


def list(account, end_date_time=None, start_date_time=None, **kwargs):
    '''
    List job recurrences in a Data Lake Analytics account.
    '''
    return call_az("az dla job recurrence list", locals())

