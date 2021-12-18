from .... pyaz_utils import _call_az

def create(name, resource_group, workspace_name, description=None, if_match=None, no_wait=None):
    '''
    Create an self-hosted integration runtime.
    '''
    return _call_az("az synapse integration-runtime self-hosted create", locals())

