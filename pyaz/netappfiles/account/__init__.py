from ... pyaz_utils import call_az
from . import ad, backup, backup_policy


def show(name, resource_group, **kwargs):
    '''
    Get the specified ANF account.
    '''
    return call_az("az netappfiles account show", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete the specified ANF account.
    '''
    return call_az("az netappfiles account delete", locals())


def list(resource_group=None, **kwargs):
    '''
    List ANF accounts by subscription or by resource group name.
    '''
    return call_az("az netappfiles account list", locals())


def create(location, name, resource_group, encryption=None, tags=None, **kwargs):
    '''
    Create a new Azure NetApp Files (ANF) account. Note that active directories are added using the subgroup commands.
    '''
    return call_az("az netappfiles account create", locals())


def update(name, resource_group, add=None, encryption=None, force_string=None, remove=None, set=None, tags=None, **kwargs):
    '''
    Set/modify the tags for a specified ANF account.
    '''
    return call_az("az netappfiles account update", locals())

