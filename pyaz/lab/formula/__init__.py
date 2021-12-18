from ... pyaz_utils import _call_az

def show(lab_name, name, resource_group, expand=None):
    '''
    Show formulae from an Azure DevTest Lab.
    '''
    return _call_az("az lab formula show", locals())


def list(lab_name, resource_group, expand=None, filter=None, orderby=None, top=None):
    return _call_az("az lab formula list", locals())


def delete(lab_name, name, resource_group):
    return _call_az("az lab formula delete", locals())


def export_artifacts(lab_name, name, resource_group):
    '''
    Export artifacts from a formula.
    '''
    return _call_az("az lab formula export-artifacts", locals())

