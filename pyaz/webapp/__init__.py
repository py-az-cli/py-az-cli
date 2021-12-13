from .. pyaz_utils import call_az
from . import auth, config, connection, cors, deleted, hybrid_connection, identity, log, traffic_routing, vnet_integration


def create(name, plan, resource_group, assign_identity=None, deployment_container_image_name=None, deployment_local_git=None, deployment_source_branch=None, deployment_source_url=None, docker_registry_server_password=None, docker_registry_server_user=None, multicontainer_config_file=None, multicontainer_config_type=None, role=None, runtime=None, scope=None, startup_file=None, subnet=None, tags=None, vnet=None, **kwargs):
    '''
    Create a web app.
    '''
    return call_az("az webapp create", locals())


def up(app_service_environment=None, dryrun=None, html=None, launch_browser=None, location=None, logs=None, name=None, os_type=None, plan=None, resource_group=None, runtime=None, sku=None, **kwargs):
    '''
    Create a webapp and deploy code from a local workspace to the app. The command is required to run from the folder where the code is present. Current support includes Node, Python, .NET Core and ASP.NET. Node, Python apps are created as Linux apps. .Net Core, ASP.NET, and static HTML apps are created as Windows apps. Append the html flag to deploy as a static HTML app.

    '''
    return call_az("az webapp up", locals())


def ssh(name, resource_group, instance=None, port=None, slot=None, timeout=None, **kwargs):
    '''
    SSH command establishes a ssh session to the web container and developer would get a shell terminal remotely.
    '''
    return call_az("az webapp ssh", locals())


def list(resource_group=None, **kwargs):
    '''
    List web apps.
    '''
    return call_az("az webapp list", locals())


def show(name, resource_group, slot=None, **kwargs):
    '''
    Get the details of a web app.
    '''
    return call_az("az webapp show", locals())


def delete(name, resource_group, keep_dns_registration=None, keep_empty_plan=None, keep_metrics=None, slot=None, **kwargs):
    '''
    Delete a web app.
    '''
    return call_az("az webapp delete", locals())


def stop(name, resource_group, slot=None, **kwargs):
    '''
    Stop a web app.
    '''
    return call_az("az webapp stop", locals())


def start(name, resource_group, slot=None, **kwargs):
    '''
    Start a web app.
    '''
    return call_az("az webapp start", locals())


def restart(name, resource_group, slot=None, **kwargs):
    '''
    Restart a web app.
    '''
    return call_az("az webapp restart", locals())


def browse(name, resource_group, logs=None, slot=None, **kwargs):
    '''
    Open a web app in a browser.
    '''
    return call_az("az webapp browse", locals())


def list_instances(name, resource_group, slot=None, **kwargs):
    '''
    List all scaled out instances of a web app or web app slot.
    '''
    return call_az("az webapp list-instances", locals())


def list_runtimes(linux=None, **kwargs):
    '''
    List available built-in stacks which can be used for web apps.
    '''
    return call_az("az webapp list-runtimes", locals())


def create_remote_connection(name, resource_group, instance=None, port=None, slot=None, timeout=None, **kwargs):
    '''
    Creates a remote connection using a tcp tunnel to your web app
    '''
    return call_az("az webapp create-remote-connection", locals())


def deploy(name, resource_group, async_=None, clean=None, ignore_stack=None, restart=None, slot=None, src_path=None, src_url=None, target_path=None, timeout=None, type=None, **kwargs):
    '''
    Deploys a provided artifact to Azure Web Apps.
    '''
    return call_az("az webapp deploy", locals())


def update(name, resource_group, add=None, client_affinity_enabled=None, force_dns_registration=None, force_string=None, https_only=None, remove=None, set=None, skip_custom_domain_verification=None, skip_dns_registration=None, slot=None, ttl_in_seconds=None, **kwargs):
    '''
    Update an existing web app.
    '''
    return call_az("az webapp update", locals())

