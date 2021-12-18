from ..... pyaz_utils import _call_az

def show(name, resource_group, zone_name, record_type=None):
    '''
    Get the details of an AAAA record set.
    '''
    return _call_az("az network dns record-set aaaa show", locals())


def delete(name, resource_group, zone_name, if_match=None, record_type=None, yes=None):
    '''
    Delete an AAAA record set and all associated records.
    '''
    return _call_az("az network dns record-set aaaa delete", locals())


def list(resource_group, zone_name, record_type=None):
    '''
    List all AAAA record sets in a zone.
    '''
    return _call_az("az network dns record-set aaaa list", locals())


def create(name, resource_group, zone_name, if_match=None, if_none_match=None, metadata=None, record_set_type=None, target_resource=None, ttl=None):
    '''
    Create an empty AAAA record set.
    '''
    return _call_az("az network dns record-set aaaa create", locals())


def add_record(ipv6_address, record_set_name, resource_group, zone_name, if_none_match=None, ttl=None):
    '''
    Add an AAAA record.
    '''
    return _call_az("az network dns record-set aaaa add-record", locals())


def remove_record(ipv6_address, record_set_name, resource_group, zone_name, keep_empty_record_set=None):
    '''
    Remove AAAA record from its record set.
    '''
    return _call_az("az network dns record-set aaaa remove-record", locals())


def update(name, resource_group, zone_name, add=None, force_string=None, if_match=None, if_none_match=None, metadata=None, record_type=None, remove=None, set=None, target_resource=None):
    '''
    Update an AAAA record set.
    '''
    return _call_az("az network dns record-set aaaa update", locals())

