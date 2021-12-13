from ... pyaz_utils import call_az

def list(account_name, asset_name, resource_group, **kwargs):
    '''
    List all the asset filters of an Azure Media Services account.
    '''
    return call_az("az ams asset-filter list", locals())


def show(account_name, asset_name, name, resource_group, **kwargs):
    '''
    Show the details of an asset filter.
    '''
    return call_az("az ams asset-filter show", locals())


def delete(account_name, asset_name, name, resource_group, **kwargs):
    '''
    Delete an asset filter.
    '''
    return call_az("az ams asset-filter delete", locals())


def create(account_name, asset_name, name, resource_group, bitrate=None, end_timestamp=None, first_quality=None, force_end_timestamp=None, live_backoff_duration=None, presentation_window_duration=None, start_timestamp=None, timescale=None, tracks=None, **kwargs):
    '''
    Create an asset filter.
    '''
    return call_az("az ams asset-filter create", locals())


def update(account_name, asset_name, name, resource_group, add=None, bitrate=None, end_timestamp=None, first_quality=None, force_end_timestamp=None, force_string=None, live_backoff_duration=None, presentation_window_duration=None, remove=None, set=None, start_timestamp=None, timescale=None, tracks=None, **kwargs):
    '''
    Update the details of an asset filter.
    '''
    return call_az("az ams asset-filter update", locals())

