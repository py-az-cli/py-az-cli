from ... pyaz_utils import call_az

def set(distribution, name, resource_group, **kwargs):
    '''
    Configure routing traffic to deployment slots.
    '''
    return call_az("az webapp traffic-routing set", locals())


def show(name, resource_group, **kwargs):
    '''
    Display the current distribution of traffic across slots.
    '''
    return call_az("az webapp traffic-routing show", locals())


def clear(name, resource_group, **kwargs):
    '''
    Clear the routing rules and send all traffic to production.
    '''
    return call_az("az webapp traffic-routing clear", locals())

