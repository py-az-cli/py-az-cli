from ... pyaz_utils import call_az

def list(resource_group=None, **kwargs):
    '''
    List all IoT Security solutions.
    '''
    return call_az("az security iot-solution list", locals())


def show(resource_group, solution_name, **kwargs):
    '''
    Shows a IoT Security solution.
    '''
    return call_az("az security iot-solution show", locals())


def create(display_name, iot_hubs, location, resource_group, solution_name, **kwargs):
    '''
    Create your IoT Security solution.
    '''
    return call_az("az security iot-solution create", locals())


def delete(resource_group, solution_name, **kwargs):
    '''
    Delete your IoT Security solution.
    '''
    return call_az("az security iot-solution delete", locals())


def update(resource_group, solution_name, display_name=None, iot_hubs=None, **kwargs):
    '''
    Update your IoT Security solution.
    '''
    return call_az("az security iot-solution update", locals())

