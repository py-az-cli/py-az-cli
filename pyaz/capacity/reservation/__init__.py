from ... pyaz_utils import _call_az
from . import group


def create(capacity_reservation_group, capacity_reservation_name, resource_group, sku, capacity=None, location=None, no_wait=None, tags=None, zone=None):
    '''
    Create capacity reservation.
    '''
    return _call_az("az capacity reservation create", locals())


def update(capacity_reservation_group, capacity_reservation_name, resource_group, capacity=None, no_wait=None, tags=None):
    '''
    Update capacity reservation.
    '''
    return _call_az("az capacity reservation update", locals())


def delete(capacity_reservation_group, capacity_reservation_name, resource_group, no_wait=None, yes=None):
    '''
    Delete capacity reservation.
    '''
    return _call_az("az capacity reservation delete", locals())


def show(capacity_reservation_group, capacity_reservation_name, resource_group, instance_view=None):
    '''
    Show capacity reservation.
    '''
    return _call_az("az capacity reservation show", locals())


def list(capacity_reservation_group, resource_group):
    '''
    List capacity reservation.
    '''
    return _call_az("az capacity reservation list", locals())

