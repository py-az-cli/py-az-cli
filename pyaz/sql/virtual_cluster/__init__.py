from ... pyaz_utils import call_az

def delete(name, resource_group, no_wait=None, **kwargs):
    '''
    Delete a virtual cluster.
    '''
    return call_az("az sql virtual-cluster delete", locals())


def show(name, resource_group, **kwargs):
    '''
    Get the details for a virtual cluster.
    '''
    return call_az("az sql virtual-cluster show", locals())


def list(resource_group=None, **kwargs):
    '''
    List available virtual clusters.
    '''
    return call_az("az sql virtual-cluster list", locals())

