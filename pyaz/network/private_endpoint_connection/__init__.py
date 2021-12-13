from ... pyaz_utils import call_az

def approve(description=None, id=None, name=None, resource_group=None, resource_name=None, type=None, **kwargs):
    '''
    Approve a private endpoint connection.
    '''
    return call_az("az network private-endpoint-connection approve", locals())


def reject(description=None, id=None, name=None, resource_group=None, resource_name=None, type=None, **kwargs):
    '''
    Reject a private endpoint connection.
    '''
    return call_az("az network private-endpoint-connection reject", locals())


def delete(id=None, name=None, resource_group=None, resource_name=None, type=None, yes=None, **kwargs):
    '''
    Delete a private endpoint connection.
    '''
    return call_az("az network private-endpoint-connection delete", locals())


def show(id=None, name=None, resource_group=None, resource_name=None, type=None, **kwargs):
    '''
    Show a private endpoint connection.
    '''
    return call_az("az network private-endpoint-connection show", locals())


def list(id=None, name=None, resource_group=None, type=None, **kwargs):
    '''
    List all private endpoint connections.
    '''
    return call_az("az network private-endpoint-connection list", locals())

