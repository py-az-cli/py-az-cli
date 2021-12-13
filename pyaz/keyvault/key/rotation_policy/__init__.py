from .... pyaz_utils import call_az

def show(hsm_name=None, id=None, name=None, vault_name=None, **kwargs):
    '''
    Get the rotation policy of a Key Vault key.
    '''
    return call_az("az keyvault key rotation-policy show", locals())


def update(value, hsm_name=None, id=None, name=None, vault_name=None, **kwargs):
    '''
    Update the rotation policy of a Key Vault key.
    '''
    return call_az("az keyvault key rotation-policy update", locals())

