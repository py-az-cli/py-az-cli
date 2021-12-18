from ..... pyaz_utils import _call_az

def list(alias, name, namespace_name, resource_group):
    '''
    Shows the keys and connection strings of Authorizationrule for the EventHubs Namespace
    '''
    return _call_az("az eventhubs georecovery-alias authorization-rule keys list", locals())

