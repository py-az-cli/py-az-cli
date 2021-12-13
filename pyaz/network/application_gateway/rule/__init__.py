from .... pyaz_utils import call_az

def list(gateway_name, resource_group, **kwargs):
    '''
    List rules.
    '''
    return call_az("az network application-gateway rule list", locals())


def show(gateway_name, name, resource_group, **kwargs):
    '''
    Get the details of a rule.
    '''
    return call_az("az network application-gateway rule show", locals())


def delete(gateway_name, name, resource_group, no_wait=None, **kwargs):
    '''
    Delete a rule.
    '''
    return call_az("az network application-gateway rule delete", locals())


def create(gateway_name, name, resource_group, address_pool=None, http_listener=None, http_settings=None, no_wait=None, priority=None, redirect_config=None, rewrite_rule_set=None, rule_type=None, url_path_map=None, **kwargs):
    '''
    Create a rule.
    '''
    return call_az("az network application-gateway rule create", locals())


def update(gateway_name, name, resource_group, add=None, address_pool=None, force_string=None, http_listener=None, http_settings=None, no_wait=None, priority=None, redirect_config=None, remove=None, rewrite_rule_set=None, rule_type=None, set=None, url_path_map=None, **kwargs):
    '''
    Update a rule.
    '''
    return call_az("az network application-gateway rule update", locals())

