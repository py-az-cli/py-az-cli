from ... pyaz_utils import call_az

def show(name, resource_group, **kwargs):
    '''
    Get the status of Classic Azure Monitor logs integration on an HDInsight cluster.
    '''
    return call_az("az hdinsight monitor show", locals())


def enable(name, resource_group, workspace, no_validation_timeout=None, primary_key=None, **kwargs):
    '''
    Enable the Classic Azure Monitor logs integration on an HDInsight cluster.
    '''
    return call_az("az hdinsight monitor enable", locals())


def disable(name, resource_group, **kwargs):
    '''
    Disable the Classic Azure Monitor logs integration on an HDInsight cluster.
    '''
    return call_az("az hdinsight monitor disable", locals())

