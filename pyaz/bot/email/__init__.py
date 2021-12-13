from ... pyaz_utils import call_az

def create(email_address, name, password, resource_group, add_disabled=None, **kwargs):
    '''
    Create the Email Channel on a bot.
    '''
    return call_az("az bot email create", locals())


def show(name, resource_group, with_secrets=None, **kwargs):
    '''
    Get details of the email Channel on a bot
    '''
    return call_az("az bot email show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete the email Channel on a bot
    '''
    return call_az("az bot email delete", locals())

