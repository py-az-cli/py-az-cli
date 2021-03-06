from ... pyaz_utils import _call_az

def list(account_name, invoice_section_name=None, profile_name=None):
    '''
    List the role assignments for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing role-assignment list", locals())


def delete(account_name, name, invoice_section_name=None, profile_name=None, yes=None):
    '''
    Delete a role assignment for the caller on a billing account. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a role assignment.

    Optional Parameters:
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    - yes -- Do not prompt for confirmation.
    '''
    return _call_az("az billing role-assignment delete", locals())


def show(account_name, name, invoice_section_name=None, profile_name=None):
    '''
    Show the role assignment detail for the caller within different scopes. The operation is supported for billing accounts with agreement type Microsoft Partner Agreement or Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a role assignment.

    Optional Parameters:
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing role-assignment show", locals())

