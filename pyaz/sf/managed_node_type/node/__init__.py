from .... pyaz_utils import call_az

def reimage(cluster_name, node_name, resource_group, force=None, **kwargs):
    '''
    Reimage nodes of a node type.
    '''
    return call_az("az sf managed-node-type node reimage", locals())


def restart(cluster_name, node_name, resource_group, force=None, **kwargs):
    '''
    Restart nodes of a node type.
    '''
    return call_az("az sf managed-node-type node restart", locals())


def delete(cluster_name, node_name, resource_group, force=None, **kwargs):
    '''
    Delete nodes of a node type.
    '''
    return call_az("az sf managed-node-type node delete", locals())

