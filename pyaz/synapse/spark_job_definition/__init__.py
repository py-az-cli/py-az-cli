from ... pyaz_utils import call_az

def list(workspace_name, **kwargs):
    '''
    List spark job definitions.
    '''
    return call_az("az synapse spark-job-definition list", locals())


def show(name, workspace_name, **kwargs):
    '''
    Get a spark job definition.
    '''
    return call_az("az synapse spark-job-definition show", locals())


def delete(name, workspace_name, no_wait=None, **kwargs):
    '''
    Delete a spark job definition.
    '''
    return call_az("az synapse spark-job-definition delete", locals())


def create(file, name, workspace_name, folder_path=None, no_wait=None, **kwargs):
    '''
    Create a spark job definition.
    '''
    return call_az("az synapse spark-job-definition create", locals())


def wait(name, workspace_name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of a spark job definition is met.
    '''
    return call_az("az synapse spark-job-definition wait", locals())


def update(file, name, workspace_name, folder_path=None, no_wait=None, **kwargs):
    '''
    Update a spark job definition.
    '''
    return call_az("az synapse spark-job-definition update", locals())

