from .... pyaz_utils import call_az

def create(access, communities, filter_name, name, resource_group, location=None, **kwargs):
    '''
    Create a rule in a route filter.
    '''
    return call_az("az network route-filter rule create", locals())


def list(filter_name, resource_group, **kwargs):
    '''
    List rules in a route filter.
    '''
    return call_az("az network route-filter rule list", locals())


def show(filter_name, name, resource_group, **kwargs):
    '''
    Get the details of a rule in a route filter.
    '''
    return call_az("az network route-filter rule show", locals())


def delete(filter_name, name, resource_group, **kwargs):
    '''
    Delete a rule from a route filter.
    '''
    return call_az("az network route-filter rule delete", locals())


def update(filter_name, name, resource_group, add=None, force_string=None, remove=None, set=None, **kwargs):
    '''
    Update a rule in a route filter.
    '''
    return call_az("az network route-filter rule update", locals())


def list_service_communities(**kwargs):
    '''
    Gets all the available BGP service communities.
    '''
    return call_az("az network route-filter rule list-service-communities", locals())

