from .... pyaz_utils import call_az

def list(group, **kwargs):
    return call_az("az ad group member list", locals())


def add(group, member_id, additional_properties=None, **kwargs):
    return call_az("az ad group member add", locals())


def remove(group, member_id, **kwargs):
    return call_az("az ad group member remove", locals())


def check(group, member_id, **kwargs):
    '''
    Check if a member is in a group.
    '''
    return call_az("az ad group member check", locals())

