from .. pyaz_utils import call_az

def install(target_platform=None, version=None, **kwargs):
    '''
    Install Bicep CLI.
    '''
    return call_az("az bicep install", locals())


def uninstall(**kwargs):
    '''
    Uninstall Bicep CLI.
    '''
    return call_az("az bicep uninstall", locals())


def upgrade(target_platform=None, **kwargs):
    '''
    Upgrade Bicep CLI to the latest version.
    '''
    return call_az("az bicep upgrade", locals())


def build(file, outdir=None, outfile=None, stdout=None, **kwargs):
    '''
    Build a Bicep file.
    '''
    return call_az("az bicep build", locals())


def decompile(file, **kwargs):
    '''
    Attempt to decompile an ARM template file to a Bicep file.
    '''
    return call_az("az bicep decompile", locals())


def publish(file, target, **kwargs):
    '''
    Publish a bicep file to a remote module registry.
    '''
    return call_az("az bicep publish", locals())


def version(**kwargs):
    '''
    Show the installed version of Bicep CLI.
    '''
    return call_az("az bicep version", locals())


def list_versions(**kwargs):
    '''
    List out all available versions of Bicep CLI.
    '''
    return call_az("az bicep list-versions", locals())

