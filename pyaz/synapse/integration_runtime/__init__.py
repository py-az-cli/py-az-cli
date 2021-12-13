from ... pyaz_utils import call_az
from . import managed, self_hosted


def list(resource_group, workspace_name, **kwargs):
    '''
    List integration runtimes.
    '''
    return call_az("az synapse integration-runtime list", locals())


def show(name, resource_group, workspace_name, if_none_match=None, **kwargs):
    '''
    Get an integration runtime.
    '''
    return call_az("az synapse integration-runtime show", locals())


def create(name, resource_group, type, workspace_name, compute_type=None, core_count=None, description=None, if_match=None, location=None, no_wait=None, time_to_live=None, **kwargs):
    '''
    Create an integration runtime.
    '''
    return call_az("az synapse integration-runtime create", locals())


def delete(name, resource_group, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    Delete an integration runtime.
    '''
    return call_az("az synapse integration-runtime delete", locals())


def update(auto_update, name, resource_group, update_delay_offset, workspace_name, **kwargs):
    '''
    Update an integration runtime.
    '''
    return call_az("az synapse integration-runtime update", locals())


def start(name, resource_group, workspace_name, no_wait=None, **kwargs):
    '''
    start an SSIS integration runtime.
    '''
    return call_az("az synapse integration-runtime start", locals())


def stop(name, resource_group, workspace_name, no_wait=None, yes=None, **kwargs):
    '''
    stop an SSIS integration runtime.
    '''
    return call_az("az synapse integration-runtime stop", locals())


def upgrade(name, resource_group, workspace_name, **kwargs):
    '''
    Upgrade self-hosted integration runtime.
    '''
    return call_az("az synapse integration-runtime upgrade", locals())


def list_auth_key(name, resource_group, workspace_name, **kwargs):
    '''
    Get keys for a self-hosted integration runtime.
    '''
    return call_az("az synapse integration-runtime list-auth-key", locals())


def regenerate_auth_key(name, resource_group, workspace_name, key_name=None, **kwargs):
    '''
    Regenerate self-hosted integration runtime key.
    '''
    return call_az("az synapse integration-runtime regenerate-auth-key", locals())


def get_monitoring_data(name, resource_group, workspace_name, **kwargs):
    '''
    Get metric data for a self-hosted integration runtime.
    '''
    return call_az("az synapse integration-runtime get-monitoring-data", locals())


def sync_credentials(name, resource_group, workspace_name, **kwargs):
    '''
    Synchronize credentials among integration runtime nodes.
    '''
    return call_az("az synapse integration-runtime sync-credentials", locals())


def get_connection_info(name, resource_group, workspace_name, **kwargs):
    '''
    Get the integration runtime connection infomation.
    '''
    return call_az("az synapse integration-runtime get-connection-info", locals())


def get_status(name, resource_group, workspace_name, **kwargs):
    '''
    Gets detailed status information for an integration runtime.
    '''
    return call_az("az synapse integration-runtime get-status", locals())


def wait(name, resource_group, workspace_name, created=None, custom=None, deleted=None, exists=None, if_none_match=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a condition of a integration runtime is met.
    '''
    return call_az("az synapse integration-runtime wait", locals())

