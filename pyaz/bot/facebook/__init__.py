from ... pyaz_utils import call_az

def create(appid, name, page_id, resource_group, secret, token, add_disabled=None, **kwargs):
    '''
    Create the Facebook Channel on a bot.
    '''
    return call_az("az bot facebook create", locals())


def show(name, resource_group, with_secrets=None, **kwargs):
    '''
    Get details of the Facebook Channel on a bot
    '''
    return call_az("az bot facebook show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete the Facebook Channel on a bot
    '''
    return call_az("az bot facebook delete", locals())

