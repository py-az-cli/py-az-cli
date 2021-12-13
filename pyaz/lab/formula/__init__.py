from ... pyaz_utils import call_az

def show(lab_name, name, resource_group, expand=None, **kwargs):
    '''
    Show formulae from an Azure DevTest Lab.
    '''
    return call_az("az lab formula show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None, **kwargs):
    return call_az("az lab formula list", locals())


def delete(lab_name, name, resource_group, **kwargs):
    return call_az("az lab formula delete", locals())


def export_artifacts(lab_name, name, resource_group, **kwargs):
    '''
    Export artifacts from a formula.
    '''
    return call_az("az lab formula export-artifacts", locals())

