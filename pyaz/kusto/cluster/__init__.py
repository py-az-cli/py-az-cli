from ... pyaz_utils import call_az

def create(name, resource_group, sku, capacity=None, location=None, no_wait=None, **kwargs):
    '''
    Create a Kusto cluster.
    '''
    return call_az("az kusto cluster create", locals())


def stop(name, resource_group, no_wait=None, **kwargs):
    '''
    Stop a Kusto cluster.
    '''
    return call_az("az kusto cluster stop", locals())


def start(name, resource_group, no_wait=None, **kwargs):
    '''
    Start a Kusto cluster.
    '''
    return call_az("az kusto cluster start", locals())


def list(resource_group, **kwargs):
    '''
    List a Kusto cluster.
    '''
    return call_az("az kusto cluster list", locals())


def show(name, resource_group, **kwargs):
    '''
    Get a Kusto cluster.
    '''
    return call_az("az kusto cluster show", locals())


def delete(name, resource_group, yes=None, **kwargs):
    '''
    Delete a Kusto cluster.
    '''
    return call_az("az kusto cluster delete", locals())


def update(name, resource_group, add=None, capacity=None, force_string=None, remove=None, set=None, sku=None, **kwargs):
    '''
    Update a Kusto cluster.
    '''
    return call_az("az kusto cluster update", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Wait for a managed Kusto cluster to reach a desired state.
    '''
    return call_az("az kusto cluster wait", locals())

