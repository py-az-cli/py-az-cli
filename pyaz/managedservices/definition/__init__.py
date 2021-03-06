'''
Manage the registration definitions in Azure.
'''
from ... pyaz_utils import _call_az

def create(name, principal_id, role_definition_id, tenant_id, definition_id=None, description=None, plan_name=None, plan_product=None, plan_publisher=None, plan_version=None):
    '''
    Creates a new registration definition.

    Required Parameters:
    - name -- None
    - principal_id -- None
    - role_definition_id -- None
    - tenant_id -- None

    Optional Parameters:
    - definition_id -- None
    - description -- None
    - plan_name -- None
    - plan_product -- None
    - plan_publisher -- None
    - plan_version -- None
    '''
    return _call_az("az managedservices definition create", locals())


def list():
    '''
    List all the registration definitions under the default scope or under the subscription provided.
    '''
    return _call_az("az managedservices definition list", locals())


def delete(definition):
    '''
    Deletes a registration.

    Required Parameters:
    - definition -- The identifier (guid) or the fully qualified resource id of the registration definition. When resource id is used, subscription id and resource group parameters are ignored.
    '''
    return _call_az("az managedservices definition delete", locals())


def show(definition):
    '''
    Gets a registration definition.

    Required Parameters:
    - definition -- The identifier (guid) or the fully qualified resource id of the registration definition. When resource id is used, subscription id and resource group parameters are ignored.
    '''
    return _call_az("az managedservices definition show", locals())

