from ... pyaz_utils import call_az

def list(assessed_resource_id=None, assessment_name=None, **kwargs):
    '''
    List all security sub assessment results.
    '''
    return call_az("az security sub-assessment list", locals())


def show(assessment_name, name, assessed_resource_id=None, **kwargs):
    '''
    Shows a security sub assessment.
    '''
    return call_az("az security sub-assessment show", locals())

