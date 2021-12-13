from ... pyaz_utils import call_az

def create(account_sid, auth_token, name, phone, resource_group, add_disabled=None, is_validated=None, **kwargs):
    '''
    Create the SMS Channel on a bot.
    '''
    return call_az("az bot sms create", locals())


def show(name, resource_group, with_secrets=None, **kwargs):
    '''
    Get details of the SMS Channel on a bot
    '''
    return call_az("az bot sms show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete the SMS Channel on a bot
    '''
    return call_az("az bot sms delete", locals())

