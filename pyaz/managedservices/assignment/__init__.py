from ... pyaz_utils import call_az

def create(definition, assignment_id=None, resource_group=None, **kwargs):
    '''
    Creates a new registration assignment.
    '''
    return call_az("az managedservices assignment create", locals())


def show(assignment, include_definition=None, resource_group=None, **kwargs):
    '''
    Gets a registration assignment.
    '''
    return call_az("az managedservices assignment show", locals())


def delete(assignment, resource_group=None, **kwargs):
    '''
    Deletes the registration assignment.
    '''
    return call_az("az managedservices assignment delete", locals())


def list(include_definition=None, resource_group=None, **kwargs):
    '''
    List all the registration assignments.
    '''
    return call_az("az managedservices assignment list", locals())

