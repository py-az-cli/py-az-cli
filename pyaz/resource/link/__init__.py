from ... pyaz_utils import call_az

def create(link, target, notes=None, **kwargs):
    '''
    Create a new link between resources.
    '''
    return call_az("az resource link create", locals())


def delete(link, **kwargs):
    '''
    Delete a link between resources.
    '''
    return call_az("az resource link delete", locals())


def show(link, **kwargs):
    return call_az("az resource link show", locals())


def list(filter=None, scope=None, **kwargs):
    '''
    List resource links.
    '''
    return call_az("az resource link list", locals())


def update(link, notes=None, target=None, **kwargs):
    '''
    Update link between resources.
    '''
    return call_az("az resource link update", locals())

