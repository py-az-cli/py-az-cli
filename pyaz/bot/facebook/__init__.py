'''
Manage the Facebook Channel on a bot.
'''
from ... pyaz_utils import _call_az

def create(appid, name, page_id, resource_group, secret, token, add_disabled=None):
    '''
    Create the Facebook Channel on a bot.

    Required Parameters:
    - appid -- The Facebook application id.
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - page_id -- Page ID of the Facebook page to be used for the bot.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - secret -- The Facebook application secret.
    - token -- The Facebook application access token.

    Optional Parameters:
    - add_disabled -- Add the channel in a disabled state
    '''
    return _call_az("az bot facebook create", locals())


def show(name, resource_group, with_secrets=None):
    '''
    Get details of the Facebook Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - with_secrets -- Show secrets in response for the channel.
    '''
    return _call_az("az bot facebook show", locals())


def delete(name, resource_group):
    '''
    Delete the Facebook Channel on a bot

    Required Parameters:
    - name -- The resource name of the bot. Bot name must be between 4 and 42 characters in length. Bot name can only have the following characters -, a - z, A - Z, 0 - 9, and _.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az bot facebook delete", locals())

