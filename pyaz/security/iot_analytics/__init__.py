from ... pyaz_utils import call_az

def list(resource_group, solution_name, **kwargs):
    '''
    List all IoT security Analytics metrics.
    '''
    return call_az("az security iot-analytics list", locals())


def show(resource_group, solution_name, **kwargs):
    '''
    Shows IoT Security Analytics metrics.
    '''
    return call_az("az security iot-analytics show", locals())

