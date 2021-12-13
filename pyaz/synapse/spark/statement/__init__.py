from .... pyaz_utils import call_az

def invoke(code, language, session_id, spark_pool_name, workspace_name, **kwargs):
    '''
    Invoke a Spark statement.
    '''
    return call_az("az synapse spark statement invoke", locals())


def list(session_id, spark_pool_name, workspace_name, **kwargs):
    '''
    List all Spark statements
    '''
    return call_az("az synapse spark statement list", locals())


def show(livy_id, session_id, spark_pool_name, workspace_name, **kwargs):
    '''
    Get a Spark statement.
    '''
    return call_az("az synapse spark statement show", locals())


def cancel(livy_id, session_id, spark_pool_name, workspace_name, yes=None, **kwargs):
    '''
    Cancel a Spark statement.
    '''
    return call_az("az synapse spark statement cancel", locals())

