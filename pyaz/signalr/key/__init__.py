from ... pyaz_utils import _call_az

def list(name, resource_group):
    '''
    List the access keys for a SignalR Service.
    '''
    return _call_az("az signalr key list", locals())


def renew(key_type, name, resource_group):
    '''
    Regenerate the access key for a SignalR Service.
    '''
    return _call_az("az signalr key renew", locals())

