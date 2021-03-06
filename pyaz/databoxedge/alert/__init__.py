'''
Manage alert with databoxedge
'''
from ... pyaz_utils import _call_az

def list(device_name, resource_group):
    '''
    Get all the alerts for a Data Box Edge/Data Box Gateway device.

    Required Parameters:
    - device_name -- The device name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge alert list", locals())


def show(device_name, name, resource_group):
    '''
    Get an alert by name.

    Required Parameters:
    - device_name -- The device name.
    - name -- The alert name.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az databoxedge alert show", locals())

