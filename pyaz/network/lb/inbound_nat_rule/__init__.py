from .... pyaz_utils import call_az

def list(lb_name, resource_group, **kwargs):
    '''
    List inbound NAT rules.
    '''
    return call_az("az network lb inbound-nat-rule list", locals())


def show(lb_name, name, resource_group, **kwargs):
    '''
    Get the details of an inbound NAT rule.
    '''
    return call_az("az network lb inbound-nat-rule show", locals())


def delete(lb_name, name, resource_group, **kwargs):
    '''
    Delete an inbound NAT rule.
    '''
    return call_az("az network lb inbound-nat-rule delete", locals())


def create(backend_port, lb_name, name, protocol, resource_group, enable_tcp_reset=None, floating_ip=None, frontend_ip_name=None, frontend_port=None, frontend_port_range_end=None, frontend_port_range_start=None, idle_timeout=None, **kwargs):
    '''
    Create an inbound NAT rule.
    '''
    return call_az("az network lb inbound-nat-rule create", locals())


def update(lb_name, name, resource_group, add=None, backend_port=None, enable_tcp_reset=None, floating_ip=None, force_string=None, frontend_ip_name=None, frontend_port=None, frontend_port_range_end=None, frontend_port_range_start=None, idle_timeout=None, protocol=None, remove=None, set=None, **kwargs):
    '''
    Update an inbound NAT rule.
    '''
    return call_az("az network lb inbound-nat-rule update", locals())

