from .... pyaz_utils import call_az

def list(name, resource_group, **kwargs):
    '''
    List shared access keys of a topic.
    '''
    return call_az("az eventgrid topic key list", locals())


def regenerate(key_name, name, resource_group, **kwargs):
    '''
    Regenerate a shared access key of a topic.
    '''
    return call_az("az eventgrid topic key regenerate", locals())

