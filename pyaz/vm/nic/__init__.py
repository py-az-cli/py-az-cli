from ... pyaz_utils import call_az

def add(nics, resource_group, vm_name, primary_nic=None, **kwargs):
    '''
    Add existing NICs to a VM.
    '''
    return call_az("az vm nic add", locals())


def remove(nics, resource_group, vm_name, primary_nic=None, **kwargs):
    '''
    Remove NICs from a VM.
    '''
    return call_az("az vm nic remove", locals())


def set(nics, resource_group, vm_name, primary_nic=None, **kwargs):
    '''
    Configure settings of a NIC attached to a VM.
    '''
    return call_az("az vm nic set", locals())


def show(nic, resource_group, vm_name, **kwargs):
    '''
    Display information for a NIC attached to a VM.
    '''
    return call_az("az vm nic show", locals())


def list(resource_group, vm_name, **kwargs):
    '''
    List the NICs available on a VM.
    '''
    return call_az("az vm nic list", locals())

