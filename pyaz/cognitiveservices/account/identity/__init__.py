from .... pyaz_utils import call_az

def assign(name, resource_group, **kwargs):
    '''
    Assign an identity of a Cognitive Services account.
    '''
    return call_az("az cognitiveservices account identity assign", locals())


def remove(name, resource_group, **kwargs):
    '''
    Remove the identity from a Cognitive Services account.
    '''
    return call_az("az cognitiveservices account identity remove", locals())


def show(name, resource_group, **kwargs):
    '''
    Show the identity of a Cognitive Services account.
    '''
    return call_az("az cognitiveservices account identity show", locals())

