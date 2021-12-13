from ..... pyaz_utils import call_az

def show(name, resource_group, zone_name, record_type=None, **kwargs):
    '''
    Get the details of an A record set.
    '''
    return call_az("az network private-dns record-set a show", locals())


def delete(name, resource_group, zone_name, if_match=None, record_type=None, yes=None, **kwargs):
    '''
    Delete an A record set and all associated records.
    '''
    return call_az("az network private-dns record-set a delete", locals())


def list(resource_group, zone_name, record_type=None, **kwargs):
    '''
    List all A record sets in a zone.
    '''
    return call_az("az network private-dns record-set a list", locals())


def create(name, resource_group, zone_name, metadata=None, record_type=None, ttl=None, **kwargs):
    '''
    Create an empty A record set.
    '''
    return call_az("az network private-dns record-set a create", locals())


def add_record(ipv4_address, record_set_name, resource_group, zone_name, **kwargs):
    '''
    Add an A record.
    '''
    return call_az("az network private-dns record-set a add-record", locals())


def remove_record(ipv4_address, record_set_name, resource_group, zone_name, keep_empty_record_set=None, **kwargs):
    '''
    Remove an A record from its record set.
    '''
    return call_az("az network private-dns record-set a remove-record", locals())


def update(name, resource_group, zone_name, add=None, force_string=None, if_match=None, metadata=None, record_type=None, remove=None, set=None, **kwargs):
    '''
    Update an A record set.
    '''
    return call_az("az network private-dns record-set a update", locals())

