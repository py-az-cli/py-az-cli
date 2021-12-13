from ... pyaz_utils import call_az

def list(name, resource_group, slot=None, **kwargs):
    '''
    list the hybrid-connections on a functionapp
    '''
    return call_az("az functionapp hybrid-connection list", locals())


def add(hybrid_connection, name, namespace, resource_group, slot=None, **kwargs):
    '''
    add an existing hybrid-connection to a functionapp
    '''
    return call_az("az functionapp hybrid-connection add", locals())


def remove(hybrid_connection, name, namespace, resource_group, slot=None, **kwargs):
    '''
    remove a hybrid-connection from a functionapp
    '''
    return call_az("az functionapp hybrid-connection remove", locals())

