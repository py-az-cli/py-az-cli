from ... pyaz_utils import call_az
from . import group


def create(capacity_reservation_group, capacity_reservation_name, resource_group, sku, capacity=None, location=None, no_wait=None, tags=None, zone=None, **kwargs):
    '''
    Create capacity reservation.
    '''
    return call_az("az capacity reservation create", locals())


def update(capacity_reservation_group, capacity_reservation_name, resource_group, capacity=None, no_wait=None, tags=None, **kwargs):
    '''
    Update capacity reservation.
    '''
    return call_az("az capacity reservation update", locals())


def delete(capacity_reservation_group, capacity_reservation_name, resource_group, no_wait=None, yes=None, **kwargs):
    '''
    Delete capacity reservation.
    '''
    return call_az("az capacity reservation delete", locals())


def show(capacity_reservation_group, capacity_reservation_name, resource_group, instance_view=None, **kwargs):
    '''
    Show capacity reservation.
    '''
    return call_az("az capacity reservation show", locals())


def list(capacity_reservation_group, resource_group, **kwargs):
    '''
    List capacity reservation.
    '''
    return call_az("az capacity reservation list", locals())

