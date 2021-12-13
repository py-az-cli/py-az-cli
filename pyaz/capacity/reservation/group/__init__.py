from .... pyaz_utils import call_az

def create(capacity_reservation_group, resource_group, location=None, tags=None, zones=None, **kwargs):
    '''
    Create capacity reservation group.
    '''
    return call_az("az capacity reservation group create", locals())


def update(capacity_reservation_group, resource_group, tags=None, **kwargs):
    '''
    Update capacity reservation group.
    '''
    return call_az("az capacity reservation group update", locals())


def delete(capacity_reservation_group, resource_group, yes=None, **kwargs):
    '''
    Delete capacity reservation group.
    '''
    return call_az("az capacity reservation group delete", locals())


def show(capacity_reservation_group, resource_group, instance_view=None, **kwargs):
    '''
    Show capacity reservation group.
    '''
    return call_az("az capacity reservation group show", locals())


def list(resource_group, vm_instance=None, vmss_instance=None, **kwargs):
    '''
    List the capacity reservation groups.
    '''
    return call_az("az capacity reservation group list", locals())

