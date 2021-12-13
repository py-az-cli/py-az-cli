from .... pyaz_utils import call_az

def list(vault_name, **kwargs):
    return call_az("az keyvault certificate contact list", locals())


def add(email, vault_name, name=None, phone=None, **kwargs):
    return call_az("az keyvault certificate contact add", locals())


def delete(email, vault_name, **kwargs):
    return call_az("az keyvault certificate contact delete", locals())

