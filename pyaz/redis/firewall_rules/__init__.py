from ... pyaz_utils import call_az

def create(end_ip, name, resource_group, rule_name, start_ip, **kwargs):
    '''
    Create a redis cache firewall rule.
    '''
    return call_az("az redis firewall-rules create", locals())


def update(end_ip, name, resource_group, rule_name, start_ip, **kwargs):
    '''
    Update a redis cache firewall rule.
    '''
    return call_az("az redis firewall-rules update", locals())


def delete(name, resource_group, rule_name, **kwargs):
    return call_az("az redis firewall-rules delete", locals())


def show(name, resource_group, rule_name, **kwargs):
    return call_az("az redis firewall-rules show", locals())


def list(name, resource_group, **kwargs):
    return call_az("az redis firewall-rules list", locals())

