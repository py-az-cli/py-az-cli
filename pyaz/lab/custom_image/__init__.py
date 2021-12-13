from ... pyaz_utils import call_az

def show(lab_name, name, resource_group, expand=None, **kwargs):
    return call_az("az lab custom-image show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None, **kwargs):
    return call_az("az lab custom-image list", locals())


def delete(lab_name, name, resource_group, **kwargs):
    return call_az("az lab custom-image delete", locals())


def create(lab_name, name, os_state, os_type, resource_group, source_vm_id, author=None, description=None, **kwargs):
    '''
    Create a custom image in a DevTest Lab.
    '''
    return call_az("az lab custom-image create", locals())

