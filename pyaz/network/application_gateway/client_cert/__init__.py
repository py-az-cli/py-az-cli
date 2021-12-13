from .... pyaz_utils import call_az

def add(data, gateway_name, name, resource_group, **kwargs):
    '''
    Add trusted client certificate of the application gateway.
    '''
    return call_az("az network application-gateway client-cert add", locals())


def remove(gateway_name, name, resource_group, **kwargs):
    '''
    Remove an existing trusted client certificate of the application gateway.
    '''
    return call_az("az network application-gateway client-cert remove", locals())


def list(gateway_name, resource_group, **kwargs):
    '''
    List the existing trusted client certificate of the application gateway.
    '''
    return call_az("az network application-gateway client-cert list", locals())


def show(gateway_name, name, resource_group, **kwargs):
    '''
    Show an existing trusted client certificate of the application gateway.
    '''
    return call_az("az network application-gateway client-cert show", locals())


def update(data, gateway_name, name, resource_group, **kwargs):
    '''
    Update trusted client certificate of the application gateway.
    '''
    return call_az("az network application-gateway client-cert update", locals())

