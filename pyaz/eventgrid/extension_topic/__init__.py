from ... pyaz_utils import call_az

def show(scope, **kwargs):
    '''
    Get the details of an extension topic.
    '''
    return call_az("az eventgrid extension-topic show", locals())

