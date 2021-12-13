from ... pyaz_utils import call_az

def show(profile_name, resource_group, security_policy_name, **kwargs):
    return call_az("az afd security-policy show", locals())


def list(profile_name, resource_group, **kwargs):
    return call_az("az afd security-policy list", locals())


def create(domains, profile_name, resource_group, security_policy_name, waf_policy, **kwargs):
    '''
    Creates a new security policy within the specified profile.
    '''
    return call_az("az afd security-policy create", locals())


def update(profile_name, resource_group, security_policy_name, domains=None, waf_policy=None, **kwargs):
    '''
    Update an existing security policy within the specified profile.
    '''
    return call_az("az afd security-policy update", locals())


def delete(profile_name, resource_group, security_policy_name, yes=None, **kwargs):
    return call_az("az afd security-policy delete", locals())

