from ... pyaz_utils import call_az

def show(profile_name, resource_group, rule_set_name, **kwargs):
    return call_az("az afd rule-set show", locals())


def list(profile_name, resource_group, **kwargs):
    return call_az("az afd rule-set list", locals())


def create(profile_name, resource_group, rule_set_name, **kwargs):
    '''
    Creates a new rule set under the specified profile.
    '''
    return call_az("az afd rule-set create", locals())


def delete(profile_name, resource_group, rule_set_name, yes=None, **kwargs):
    '''
    Delete the rule set.
    '''
    return call_az("az afd rule-set delete", locals())

