from .... pyaz_utils import call_az

def add(cluster_name, resource_group, common_name=None, is_admin=None, issuer_thumbprint=None, thumbprint=None, **kwargs):
    '''
    Add a new client certificate to the managed cluster.
    '''
    return call_az("az sf managed-cluster client-certificate add", locals())


def delete(cluster_name, resource_group, common_name=None, thumbprint=None, **kwargs):
    '''
    Delete a client certificate from the managed cluster.
    '''
    return call_az("az sf managed-cluster client-certificate delete", locals())

