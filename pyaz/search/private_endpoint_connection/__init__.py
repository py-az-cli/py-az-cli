from ... pyaz_utils import _call_az

def list(resource_group, service_name):
    return _call_az("az search private-endpoint-connection list", locals())


def show(private_endpoint_connection_name, resource_group, service_name):
    return _call_az("az search private-endpoint-connection show", locals())


def delete(private_endpoint_connection_name, resource_group, service_name, yes=None):
    return _call_az("az search private-endpoint-connection delete", locals())


def update(actions_required, description, name, resource_group, service_name, status):
    return _call_az("az search private-endpoint-connection update", locals())

