from .... pyaz_utils import call_az

def show(name, resource_group, **kwargs):
    return call_az("az eventgrid partner registration show", locals())


def delete(name, resource_group, yes=None, **kwargs):
    return call_az("az eventgrid partner registration delete", locals())


def list(odata_query=None, resource_group=None, **kwargs):
    '''
    List all partner registrations in specific resource group or all under the specified azure subscription.
    '''
    return call_az("az eventgrid partner registration list", locals())


def create(name, partner_name, resource_group, resource_type_name, authorized_subscription_ids=None, customer_service_extension=None, customer_service_number=None, customer_service_uri=None, description=None, display_name=None, logo_uri=None, long_description=None, setup_uri=None, tags=None, **kwargs):
    '''
    Create a new partner registration.
    '''
    return call_az("az eventgrid partner registration create", locals())

