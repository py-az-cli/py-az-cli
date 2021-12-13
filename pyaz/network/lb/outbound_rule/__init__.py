from .... pyaz_utils import call_az

def create(address_pool, frontend_ip_configs, lb_name, name, protocol, resource_group, enable_tcp_reset=None, idle_timeout=None, outbound_ports=None, **kwargs):
    '''
    Create an outbound-rule.
    '''
    return call_az("az network lb outbound-rule create", locals())


def update(lb_name, name, resource_group, add=None, address_pool=None, enable_tcp_reset=None, force_string=None, frontend_ip_configs=None, idle_timeout=None, outbound_ports=None, protocol=None, remove=None, set=None, **kwargs):
    '''
    Update an outbound-rule.
    '''
    return call_az("az network lb outbound-rule update", locals())


def list(lb_name, resource_group, **kwargs):
    '''
    List outbound rules.
    '''
    return call_az("az network lb outbound-rule list", locals())


def show(lb_name, name, resource_group, **kwargs):
    '''
    Get the details of an outbound rule.
    '''
    return call_az("az network lb outbound-rule show", locals())


def delete(lb_name, name, resource_group, **kwargs):
    '''
    Delete an outbound-rule.
    '''
    return call_az("az network lb outbound-rule delete", locals())

