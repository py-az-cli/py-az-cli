from ... pyaz_utils import call_az

def create(client_id, client_secret, name, resource_group, verification_token, add_disabled=None, landing_page_url=None, **kwargs):
    '''
    Create the Slack Channel on a bot.
    '''
    return call_az("az bot slack create", locals())


def show(name, resource_group, with_secrets=None, **kwargs):
    '''
    Get details of the Slack Channel on a bot
    '''
    return call_az("az bot slack show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete the Slack Channel on a bot
    '''
    return call_az("az bot slack delete", locals())

