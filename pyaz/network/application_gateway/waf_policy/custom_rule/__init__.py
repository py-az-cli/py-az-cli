from ..... pyaz_utils import call_az
from . import match_condition


def create(action, name, policy_name, priority, resource_group, rule_type, **kwargs):
    '''
    Create an application gateway WAF policy custom rule.
    '''
    return call_az("az network application-gateway waf-policy custom-rule create", locals())


def delete(name, policy_name, resource_group, **kwargs):
    '''
    Delete an application gateway WAF policy custom rule.
    '''
    return call_az("az network application-gateway waf-policy custom-rule delete", locals())


def list(policy_name, resource_group, **kwargs):
    '''
    List application gateway WAF policy custom rules.
    '''
    return call_az("az network application-gateway waf-policy custom-rule list", locals())


def show(name, policy_name, resource_group, **kwargs):
    '''
    Get the details of an application gateway WAF policy custom rule.
    '''
    return call_az("az network application-gateway waf-policy custom-rule show", locals())


def update(name, policy_name, resource_group, action=None, add=None, force_string=None, priority=None, remove=None, rule_type=None, set=None, **kwargs):
    '''
    Update an application gateway WAF policy custom rule.
    '''
    return call_az("az network application-gateway waf-policy custom-rule update", locals())

