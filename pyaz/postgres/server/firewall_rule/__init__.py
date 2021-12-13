from .... pyaz_utils import call_az

def create(end_ip_address, name, resource_group, server_name, start_ip_address, **kwargs):
    '''
    Create a new firewall rule for a server.
    '''
    return call_az("az postgres server firewall-rule create", locals())


def delete(name, resource_group, server_name, yes=None, **kwargs):
    '''
    Delete a firewall rule.
    '''
    return call_az("az postgres server firewall-rule delete", locals())


def show(name, resource_group, server_name, **kwargs):
    '''
    Get the details of a firewall rule.
    '''
    return call_az("az postgres server firewall-rule show", locals())


def list(resource_group, server_name, **kwargs):
    '''
    List all firewall rules for a server.
    '''
    return call_az("az postgres server firewall-rule list", locals())


def update(name, resource_group, server_name, add=None, end_ip_address=None, force_string=None, remove=None, set=None, start_ip_address=None, **kwargs):
    '''
    Update a firewall rule.
    '''
    return call_az("az postgres server firewall-rule update", locals())

