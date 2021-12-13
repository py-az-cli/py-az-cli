from .... pyaz_utils import call_az

def create(capacity_reservation_group, resource_group, location=None, tags=None, zones=None):
    '''
    Create capacity reservation group.
    '''
    return call_az("az capacity reservation group create", locals())


def update(capacity_reservation_group, resource_group, tags=None):
    '''
    Update capacity reservation group.
    '''
    return call_az("az capacity reservation group update", locals())


def delete(capacity_reservation_group, resource_group, yes=None):
    '''
    Delete capacity reservation group.
    '''
    return call_az("az capacity reservation group delete", locals())


def show(capacity_reservation_group, resource_group, instance_view=None):
    '''
    Show capacity reservation group.
    '''
    return call_az("az capacity reservation group show", locals())


def list(resource_group, vm_instance=None, vmss_instance=None):
    '''
    List the capacity reservation groups.
    '''
    return call_az("az capacity reservation group list", locals())

