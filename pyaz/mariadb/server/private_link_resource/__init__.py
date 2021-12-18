from .... pyaz_utils import _call_az

def list(resource_group, server_name):
    '''
    List the private link resources supported for a MariaDB server.
    '''
    return _call_az("az mariadb server private-link-resource list", locals())

