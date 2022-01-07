from ... pyaz_utils import _call_az

def create(name, registry, description=None, gateway=None, repository=None, resource_group=None):
    '''
    Create a scope map for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the scope map.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - description -- Description for the scope map. Maximum 256 characters are allowed.
    - gateway -- gateway permissions. Use the format "--gateway GATEWAY [ACTION1 ACTION2 ...]" per flag. Valid actions are {'config/read', 'message/write', 'config/write', 'message/read'}
    - repository -- repository permissions. Use the format "--repository REPO [ACTION1 ACTION2 ...]" per flag. Valid actions are {'content/read', 'content/write', 'metadata/write', 'metadata/read', 'content/delete'}
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr scope-map create", locals())


def delete(name, registry, resource_group=None, yes=None):
    '''
    Delete a scope map for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the scope map.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az acr scope-map delete", locals())


def update(name, registry, add_gateway=None, add_repository=None, description=None, remove_gateway=None, remove_repository=None, resource_group=None):
    '''
    Update a scope map for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the scope map.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - add_gateway -- gateway permissions to be added. Use the format "--add-gateway GATEWAY [ACTION1 ACTION2 ...]" per flag. Valid actions are {'config/read', 'message/write', 'config/write', 'message/read'}
    - add_repository -- repository permissions to be added. Use the format "--add-repository REPO [ACTION1 ACTION2 ...]" per flag. Valid actions are {'content/read', 'content/write', 'metadata/write', 'metadata/read', 'content/delete'}
    - description -- Description for the scope map. Maximum 256 characters are allowed.
    - remove_gateway -- gateway permissions to be removed. Use the format "--remove-gateway GATEWAY [ACTION1 ACTION2 ...]" per flag. Valid actions are {'config/read', 'message/write', 'config/write', 'message/read'}
    - remove_repository -- respsitory permissions to be removed. Use the format "--remove-repository REPO [ACTION1 ACTION2 ...]" per flag. Valid actions are {'content/read', 'content/write', 'metadata/write', 'metadata/read', 'content/delete'}
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr scope-map update", locals())


def show(name, registry, resource_group=None):
    '''
    Show details and attributes of a scope map for an Azure Container Registry.

    Required Parameters:
    - name -- The name of the scope map.
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr scope-map show", locals())


def list(registry, resource_group=None):
    '''
    List all scope maps for an Azure Container Registry.

    Required Parameters:
    - registry -- The name of the container registry. You can configure the default registry name using `az configure --defaults acr=<registry name>`

    Optional Parameters:
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az acr scope-map list", locals())

