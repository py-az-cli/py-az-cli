from .... pyaz_utils import call_az

def create(name, resource_group, server, end_ip_address=None, start_ip_address=None, **kwargs):
    '''
    Create a firewall rule.
    '''
    return call_az("az sql server firewall-rule create", locals())


def update(name, resource_group, server, end_ip_address=None, start_ip_address=None, **kwargs):
    '''
    Update a firewall rule.
    '''
    return call_az("az sql server firewall-rule update", locals())


def delete(name, resource_group, server, **kwargs):
    return call_az("az sql server firewall-rule delete", locals())


def show(name, resource_group, server, **kwargs):
    '''
    Shows the details for a firewall rule.
    '''
    return call_az("az sql server firewall-rule show", locals())


def list(resource_group, server, **kwargs):
    '''
    List a server's firewall rules.
    '''
    return call_az("az sql server firewall-rule list", locals())

