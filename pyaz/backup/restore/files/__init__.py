from .... pyaz_utils import call_az

def mount_rp(container_name, item_name, resource_group, rp_name, vault_name, **kwargs):
    '''
    Download a script which mounts files of a recovery point.
    '''
    return call_az("az backup restore files mount-rp", locals())


def unmount_rp(container_name, item_name, resource_group, rp_name, vault_name, **kwargs):
    '''
    Close access to the recovery point.
    '''
    return call_az("az backup restore files unmount-rp", locals())

