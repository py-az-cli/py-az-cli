from .... pyaz_utils import call_az

def create(name, policy_name, resource_group, service, service_resources, description=None, **kwargs):
    '''
    Create a service endpoint policy definition.
    '''
    return call_az("az network service-endpoint policy-definition create", locals())


def delete(name, policy_name, resource_group, **kwargs):
    '''
    Delete a service endpoint policy definition.
    '''
    return call_az("az network service-endpoint policy-definition delete", locals())


def list(policy_name, resource_group, **kwargs):
    '''
    List service endpoint policy definitions.
    '''
    return call_az("az network service-endpoint policy-definition list", locals())


def show(name, policy_name, resource_group, **kwargs):
    '''
    Get the details of a service endpoint policy definition.
    '''
    return call_az("az network service-endpoint policy-definition show", locals())


def update(name, policy_name, resource_group, add=None, description=None, force_string=None, remove=None, service=None, service_resources=None, set=None, **kwargs):
    '''
    Update a service endpoint policy definition.
    '''
    return call_az("az network service-endpoint policy-definition update", locals())

