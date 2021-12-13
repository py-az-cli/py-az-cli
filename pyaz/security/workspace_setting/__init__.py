from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
    '''
    return call_az("az security workspace-setting list", locals())


def show(name, **kwargs):
    '''
    Shows the workspace settings in your subscription - these settings let you control which workspace will hold your security data
    '''
    return call_az("az security workspace-setting show", locals())


def create(name, target_workspace, **kwargs):
    '''
    Creates a workspace settings in your subscription - these settings let you control which workspace will hold your security data
    '''
    return call_az("az security workspace-setting create", locals())


def delete(name, **kwargs):
    '''
    Deletes the workspace settings in your subscription - this will make the security events on the subscription be reported to the default workspace
    '''
    return call_az("az security workspace-setting delete", locals())

