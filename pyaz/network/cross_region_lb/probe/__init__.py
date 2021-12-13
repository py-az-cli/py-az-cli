from .... pyaz_utils import call_az

def list(lb_name, resource_group, **kwargs):
    '''
    List probes.
    '''
    return call_az("az network cross-region-lb probe list", locals())


def show(lb_name, name, resource_group, **kwargs):
    '''
    Get the details of a probe.
    '''
    return call_az("az network cross-region-lb probe show", locals())


def delete(lb_name, name, resource_group, **kwargs):
    '''
    Delete a probe.
    '''
    return call_az("az network cross-region-lb probe delete", locals())


def create(lb_name, name, port, protocol, resource_group, interval=None, path=None, threshold=None, **kwargs):
    '''
    Create a probe.
    '''
    return call_az("az network cross-region-lb probe create", locals())


def update(lb_name, name, resource_group, add=None, force_string=None, interval=None, path=None, port=None, protocol=None, remove=None, set=None, threshold=None, **kwargs):
    '''
    Update a probe.
    '''
    return call_az("az network cross-region-lb probe update", locals())

