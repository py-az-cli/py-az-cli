'''
Configure the Azure Virtual Machine Scale Set diagnostics extension.
'''
from ... pyaz_utils import _call_az

def set(resource_group, settings, vmss_name, no_auto_upgrade_minor_version=None, protected_settings=None, version=None):
    '''
    Enable diagnostics on a VMSS.

    Required Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - settings -- json string or a file path, which defines data to be collected.
    - vmss_name -- Scale set name

    Optional Parameters:
    - no_auto_upgrade_minor_version -- If set, the extension service will not automatically pick or upgrade to the latest minor version, even if the extension is redeployed.
    - protected_settings -- json string or a file path containing private configurations such as storage account keys, etc.
    - version -- version of the diagnostics extension. Will use the latest if not specfied
    '''
    return _call_az("az vmss diagnostics set", locals())


def get_default_config(is_windows_os=None):
    '''
    Show the default config file which defines data to be collected.

    Optional Parameters:
    - is_windows_os -- for Windows VMs
    '''
    return _call_az("az vmss diagnostics get-default-config", locals())

