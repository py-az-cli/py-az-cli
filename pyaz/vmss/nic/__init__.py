from ... pyaz_utils import call_az

def list(resource_group, vmss_name, **kwargs):
    return call_az("az vmss nic list", locals())


def list_vm_nics(instance_id, resource_group, vmss_name, **kwargs):
    return call_az("az vmss nic list-vm-nics", locals())


def show(instance_id, name, resource_group, vmss_name, expand=None, **kwargs):
    return call_az("az vmss nic show", locals())

