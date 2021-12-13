from ... pyaz_utils import call_az

def list(cluster_name, resource_group, **kwargs):
    '''
    List the hosts of the specified HDInsight cluster.
    '''
    return call_az("az hdinsight host list", locals())


def restart(cluster_name, host_names, resource_group, yes=None, **kwargs):
    '''
    Restart the specific hosts of the specified HDInsight cluster.
    '''
    return call_az("az hdinsight host restart", locals())

