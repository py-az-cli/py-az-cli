from .. pyaz_utils import call_az
from . import config, cors, function, hybrid_connection, identity, keys, plan, vnet_integration


def create(name, resource_group, storage_account, app_insights=None, app_insights_key=None, assign_identity=None, consumption_plan_location=None, deployment_container_image_name=None, deployment_local_git=None, deployment_source_branch=None, deployment_source_url=None, disable_app_insights=None, docker_registry_server_password=None, docker_registry_server_user=None, functions_version=None, os_type=None, plan=None, role=None, runtime=None, runtime_version=None, scope=None, subnet=None, tags=None, vnet=None, **kwargs):
    '''
    Create a function app.
    '''
    return call_az("az functionapp create", locals())


def list(resource_group=None, **kwargs):
    '''
    List function apps.
    '''
    return call_az("az functionapp list", locals())


def show(name, resource_group, slot=None, **kwargs):
    '''
    Get the details of a function app.
    '''
    return call_az("az functionapp show", locals())


def delete(name, resource_group, slot=None, **kwargs):
    '''
    Delete a function app.
    '''
    return call_az("az functionapp delete", locals())


def stop(name, resource_group, slot=None, **kwargs):
    '''
    Stop a function app.
    '''
    return call_az("az functionapp stop", locals())


def start(name, resource_group, slot=None, **kwargs):
    '''
    Start a function app.
    '''
    return call_az("az functionapp start", locals())


def restart(name, resource_group, slot=None, **kwargs):
    '''
    Restart a function app.
    '''
    return call_az("az functionapp restart", locals())


def list_consumption_locations(**kwargs):
    '''
    List available locations for running function apps.
    '''
    return call_az("az functionapp list-consumption-locations", locals())


def deploy(name, resource_group, async_=None, clean=None, ignore_stack=None, restart=None, slot=None, src_path=None, src_url=None, target_path=None, timeout=None, type=None, **kwargs):
    '''
    Deploys a provided artifact to Azure functionapp.
    '''
    return call_az("az functionapp deploy", locals())


def update(name, resource_group, add=None, force=None, force_string=None, plan=None, remove=None, set=None, slot=None, **kwargs):
    '''
    Update a function app.
    '''
    return call_az("az functionapp update", locals())

