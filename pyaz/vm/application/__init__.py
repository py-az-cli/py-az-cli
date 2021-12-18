from ... pyaz_utils import _call_az

def set(app_version_ids, name, resource_group, app_config_overrides=None, order_applications=None):
    '''
    Set appliations for VM.
    '''
    return _call_az("az vm application set", locals())


def list(resource_group, vm_name):
    '''
    List applications for VM
    '''
    return _call_az("az vm application list", locals())

