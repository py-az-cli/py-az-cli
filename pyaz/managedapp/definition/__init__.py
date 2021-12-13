from ... pyaz_utils import call_az

def create(authorizations, description, display_name, lock_level, name, resource_group, create_ui_definition=None, location=None, main_template=None, package_file_uri=None, tags=None, **kwargs):
    '''
    Create a managed application definition.
    '''
    return call_az("az managedapp definition create", locals())


def update(authorizations, description, display_name, lock_level, name, resource_group, create_ui_definition=None, location=None, main_template=None, package_file_uri=None, tags=None, **kwargs):
    '''
    Update a managed application definition.
    '''
    return call_az("az managedapp definition update", locals())


def delete(name, resource_group, **kwargs):
    '''
    Delete a managed application definition.
    '''
    return call_az("az managedapp definition delete", locals())


def show(name=None, resource_group=None, **kwargs):
    return call_az("az managedapp definition show", locals())


def list(resource_group, **kwargs):
    '''
    List managed application definitions.
    '''
    return call_az("az managedapp definition list", locals())

