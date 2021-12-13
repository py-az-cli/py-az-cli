from ... pyaz_utils import call_az

def convert(name, resource_group, **kwargs):
    '''
    Convert an Azure Availability Set to contain VMs with managed disks.
    '''
    return call_az("az vm availability-set convert", locals())


def create(name, resource_group, location=None, no_wait=None, platform_fault_domain_count=None, platform_update_domain_count=None, ppg=None, tags=None, unmanaged=None, validate=None, **kwargs):
    '''
    Create an Azure Availability Set.
    '''
    return call_az("az vm availability-set create", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete an availability set.
    '''
    return call_az("az vm availability-set delete", locals())


def list(resource_group=None, **kwargs):
    '''
    List availability sets.
    '''
    return call_az("az vm availability-set list", locals())


def list_sizes(name, resource_group, **kwargs):
    '''
    List VM sizes for an availability set.
    '''
    return call_az("az vm availability-set list-sizes", locals())


def show(name, resource_group, **kwargs):
    '''
    Get information for an availability set.
    '''
    return call_az("az vm availability-set show", locals())


def update(name, resource_group, add=None, force_string=None, ppg=None, remove=None, set=None, **kwargs):
    '''
    Update an Azure Availability Set.
    '''
    return call_az("az vm availability-set update", locals())

