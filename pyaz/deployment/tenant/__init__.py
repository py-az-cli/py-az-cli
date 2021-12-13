from ... pyaz_utils import call_az

def list(filter=None, **kwargs):
    '''
    List deployments at tenant scope.
    '''
    return call_az("az deployment tenant list", locals())


def show(name, **kwargs):
    '''
    Show a deployment at tenant scope.
    '''
    return call_az("az deployment tenant show", locals())


def delete(name, no_wait=None, **kwargs):
    '''
    Delete a deployment at tenant scope.
    '''
    return call_az("az deployment tenant delete", locals())


def validate(location, handle_extended_json_format=None, name=None, no_prompt=None, parameters=None, query_string=None, template_file=None, template_spec=None, template_uri=None, **kwargs):
    '''
    Validate whether a template is valid at tenant scope.
    '''
    return call_az("az deployment tenant validate", locals())


def create(location, confirm_with_what_if=None, handle_extended_json_format=None, name=None, no_prompt=None, no_wait=None, parameters=None, proceed_if_no_change=None, query_string=None, template_file=None, template_spec=None, template_uri=None, what_if=None, what_if_exclude_change_types=None, what_if_result_format=None, **kwargs):
    '''
    Start a deployment at tenant scope.
    '''
    return call_az("az deployment tenant create", locals())


def what_if(location, exclude_change_types=None, name=None, no_pretty_print=None, no_prompt=None, parameters=None, query_string=None, result_format=None, template_file=None, template_spec=None, template_uri=None, **kwargs):
    '''
    Execute a deployment What-If operation at tenant scope.
    '''
    return call_az("az deployment tenant what-if", locals())


def export(name, **kwargs):
    '''
    Export the template used for a deployment.
    '''
    return call_az("az deployment tenant export", locals())


def wait(name, created=None, custom=None, deleted=None, exists=None, interval=None, timeout=None, updated=None, **kwargs):
    '''
    Place the CLI in a waiting state until a deployment condition is met.
    '''
    return call_az("az deployment tenant wait", locals())


def cancel(name, **kwargs):
    '''
    Cancel a deployment at tenant scope.
    '''
    return call_az("az deployment tenant cancel", locals())

