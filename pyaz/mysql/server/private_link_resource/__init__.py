from .... pyaz_utils import call_az

def list(resource_group, server_name, **kwargs):
    '''
    List the private link resources supported for a MySQL server.
    '''
    return call_az("az mysql server private-link-resource list", locals())

