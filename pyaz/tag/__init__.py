from .. pyaz_utils import call_az

def list(resource_id=None, **kwargs):
    '''
    List the entire set of tags on a specific resource.
    '''
    return call_az("az tag list", locals())


def create(name=None, resource_id=None, tags=None, **kwargs):
    '''
    Create tags on a specific resource.
    '''
    return call_az("az tag create", locals())


def delete(name=None, resource_id=None, yes=None, **kwargs):
    '''
    Delete tags on a specific resource.
    '''
    return call_az("az tag delete", locals())


def update(operation, resource_id, tags, **kwargs):
    '''
    Selectively update the set of tags on a specific resource.
    '''
    return call_az("az tag update", locals())


def add_value(name, value, **kwargs):
    '''
    Create a tag value.
    '''
    return call_az("az tag add-value", locals())


def remove_value(name, value, **kwargs):
    return call_az("az tag remove-value", locals())

