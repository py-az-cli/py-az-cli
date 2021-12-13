from .... pyaz_utils import call_az

def show(resource_group, server, **kwargs):
    '''
    Gets a server's secure connection policy.
    '''
    return call_az("az sql server conn-policy show", locals())


def update(connection_type, resource_group, server, **kwargs):
    '''
    Updates a server's secure connection policy.
    '''
    return call_az("az sql server conn-policy update", locals())

