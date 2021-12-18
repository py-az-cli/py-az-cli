from ... pyaz_utils import _call_az

def list(billing_period_name=None, end_date=None, start_date=None, top=None):
    '''
    List the marketplace for an Azure subscription within a billing period.
    '''
    return _call_az("az consumption marketplace list", locals())

