from ... pyaz_utils import call_az
from . import namespace


def create(name, resource_group, capacity=None, location=None, tags=None, **kwargs):
    '''
    Create EventHubs Cluster
    '''
    return call_az("az eventhubs cluster create", locals())


def show(name, resource_group, **kwargs):
    '''
    Get the resource description of the specified Event Hubs Cluster.
    '''
    return call_az("az eventhubs cluster show", locals())


def list(resource_group, **kwargs):
    '''
    List the available Event Hubs Clusters within an ARM resource group.
    '''
    return call_az("az eventhubs cluster list", locals())


def wait(name, resource_group, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of the Cluster operation is completed.
    '''
    return call_az("az eventhubs cluster wait", locals())


def delete(name, resource_group, no_wait=None, yes=None, **kwargs):
    '''
    Delete an existing Event Hubs Cluster.
    '''
    return call_az("az eventhubs cluster delete", locals())


def available_region(**kwargs):
    '''
    List the quantity of available pre-provisioned Event Hubs Clusters, indexed by Azure region.
    '''
    return call_az("az eventhubs cluster available-region", locals())


def update(name, resource_group, add=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Update tags of EventHubs Cluster
    '''
    return call_az("az eventhubs cluster update", locals())

