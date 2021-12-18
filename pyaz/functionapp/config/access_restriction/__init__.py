from .... pyaz_utils import _call_az

def show(name, resource_group, slot=None):
    '''
    Show Access Restriction settings for functionapp.
    '''
    return _call_az("az functionapp config access-restriction show", locals())


def add(name, priority, resource_group, action=None, description=None, http_headers=None, ignore_missing_endpoint=None, ip_address=None, rule_name=None, scm_site=None, service_tag=None, slot=None, subnet=None, vnet_name=None, vnet_resource_group=None):
    '''
    Adds an Access Restriction to the functionapp
    '''
    return _call_az("az functionapp config access-restriction add", locals())


def remove(name, resource_group, action=None, ip_address=None, rule_name=None, scm_site=None, service_tag=None, slot=None, subnet=None, vnet_name=None):
    '''
    Removes an Access Restriction from the functionapp.
    '''
    return _call_az("az functionapp config access-restriction remove", locals())


def set(name, resource_group, use_same_restrictions_for_scm_site, slot=None):
    '''
    Sets if SCM site is using the same restrictions as the main site.
    '''
    return _call_az("az functionapp config access-restriction set", locals())

