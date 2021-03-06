from .... pyaz_utils import _call_az

def create(managed_instance, resource_group, display_name=None, object_id=None):
    '''
    Creates a new managed instance Active Directory administrator.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - display_name -- Display name of the Azure AD administrator user or group.
    - object_id -- The unique ID of the Azure AD administrator.
    '''
    return _call_az("az sql mi ad-admin create", locals())


def list(managed_instance, resource_group):
    '''
    Returns a list of managed instance Active Directory Administrators.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi ad-admin list", locals())


def delete(managed_instance, resource_group):
    '''
    Deletes an existing managed instance Active Directory Administrator.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az sql mi ad-admin delete", locals())


def update(managed_instance, resource_group, display_name=None, object_id=None):
    '''
    Updates an existing managed instance Active Directory administrator.

    Required Parameters:
    - managed_instance -- Name of the Azure SQL managed instance.
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - display_name -- Display name of the Azure AD administrator user or group.
    - object_id -- The unique ID of the Azure AD administrator.
    '''
    return _call_az("az sql mi ad-admin update", locals())

