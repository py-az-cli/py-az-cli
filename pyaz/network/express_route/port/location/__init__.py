from ..... pyaz_utils import call_az

def list(**kwargs):
    '''
    List ExpressRoute port locations.
    '''
    return call_az("az network express-route port location list", locals())


def show(location, **kwargs):
    '''
    Get the details of an ExpressRoute port location.
    '''
    return call_az("az network express-route port location show", locals())

