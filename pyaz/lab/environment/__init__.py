from ... pyaz_utils import call_az

def show(lab_name, name, resource_group, expand=None, **kwargs):
    '''
    Get the details for an environment of a lab.
    '''
    return call_az("az lab environment show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None, **kwargs):
    '''
    List environments in a lab.
    '''
    return call_az("az lab environment list", locals())


def delete(lab_name, name, resource_group, **kwargs):
    '''
    Delete an environment from a lab.
    '''
    return call_az("az lab environment delete", locals())


def create(arm_template, lab_name, name, resource_group, artifact_source_name=None, parameters=None, tags=None, **kwargs):
    '''
    Create an environment in a lab.
    '''
    return call_az("az lab environment create", locals())

