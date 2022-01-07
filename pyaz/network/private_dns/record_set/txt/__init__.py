from ..... pyaz_utils import _call_az

def show(name, resource_group, zone_name, record_type=None):
    '''
    Get the details of a TXT record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network private-dns record-set txt show", locals())


def delete(name, resource_group, zone_name, if_match=None, record_type=None, yes=None):
    '''
    Delete a TXT record set and all associated records.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - if_match -- The ETag of the record set. Omit this value to always delete the current record set. Specify the last-seen ETag value to prevent accidentally deleting any concurrent changes.
    - record_type -- ==SUPPRESS==
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az network private-dns record-set txt delete", locals())


def list(resource_group, zone_name, record_type=None):
    '''
    List all TXT record sets in a zone.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - record_type -- ==SUPPRESS==
    '''
    return _call_az("az network private-dns record-set txt list", locals())


def create(name, resource_group, zone_name, metadata=None, record_type=None, ttl=None):
    '''
    Create an empty TXT record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - record_type -- ==SUPPRESS==
    - ttl -- Record set TTL (time-to-live)
    '''
    return _call_az("az network private-dns record-set txt create", locals())


def add_record(record_set_name, resource_group, value, zone_name):
    '''
    Add a TXT record.

    Required Parameters:
    - record_set_name -- The name of the record set relative to the zone. Creates a new record set if one does not exist.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - value -- Space-separated list of text values which will be concatenated together.
    - zone_name -- The name of the Private DNS zone.
    '''
    return _call_az("az network private-dns record-set txt add-record", locals())


def remove_record(record_set_name, resource_group, value, zone_name, keep_empty_record_set=None):
    '''
    Remove a TXT record from its record set.

    Required Parameters:
    - record_set_name -- The name of the record set relative to the zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - value -- Space-separated list of text values which will be concatenated together.
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - keep_empty_record_set -- Keep the empty record set if the last record is removed.
    '''
    return _call_az("az network private-dns record-set txt remove-record", locals())


def update(name, resource_group, zone_name, add=None, force_string=None, if_match=None, metadata=None, record_type=None, remove=None, set=None):
    '''
    Update a TXT record set.

    Required Parameters:
    - name -- The name of the record set, relative to the name of the Private DNS zone.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - zone_name -- The name of the Private DNS zone.

    Optional Parameters:
    - add -- Add an object to a list of objects by specifying a path and key value pairs.  Example: --add property.listProperty <key=value, string or JSON string>
    - force_string -- When using 'set' or 'add', preserve string literals instead of attempting to convert to JSON.
    - if_match -- The ETag of the record set. Omit this value to always overwrite the current record set. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes.
    - metadata -- Metadata in space-separated key=value pairs. This overwrites any existing metadata.
    - record_type -- ==SUPPRESS==
    - remove -- Remove a property or an element from a list.  Example: --remove property.list <indexToRemove> OR --remove propertyToRemove
    - set -- Update an object by specifying a property path and value to set.  Example: --set property1.property2=<value>
    '''
    return _call_az("az network private-dns record-set txt update", locals())

