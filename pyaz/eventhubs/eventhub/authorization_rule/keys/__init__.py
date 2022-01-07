from ..... pyaz_utils import _call_az

def list(eventhub_name, name, namespace_name, resource_group):
    '''
    Shows the connection strings of Authorizationrule for the Eventhub.

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - name -- Name of EventHub AuthorizationRule
    - namespace_name -- Name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`
    '''
    return _call_az("az eventhubs eventhub authorization-rule keys list", locals())


def renew(eventhub_name, key, name, namespace_name, resource_group, key_value=None):
    '''
    Regenerate the connection strings of Authorizationrule for the namespace.

    Required Parameters:
    - eventhub_name -- Name of EventHub
    - key -- specifies Primary or Secondary key needs to be reset
    - name -- Name of Authorization Rule
    - namespace_name -- name of Namespace
    - resource_group -- Name of resource group. You can configure the default group using `az configure --defaults group=<name>`

    Optional Parameters:
    - key_value -- Optional, if the key value provided, is set for KeyType or autogenerated Key value set for keyType.
    '''
    return _call_az("az eventhubs eventhub authorization-rule keys renew", locals())

