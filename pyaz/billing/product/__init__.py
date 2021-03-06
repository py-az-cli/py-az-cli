'''
billing product
'''
from ... pyaz_utils import _call_az

def list(account_name, customer_name=None, filter=None, invoice_section_name=None, profile_name=None):
    '''
    List the products for a billing account. These don't include products billed based on usage. The operation is supported for billing accounts with agreement type Microsoft Customer Agreement or Microsoft Partner Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.

    Optional Parameters:
    - customer_name -- The ID that uniquely identifies a customer.
    - filter -- May be used to filter by product type. The filter supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not currently support 'ne', 'or', or 'not'. Tag filter is a key value pair string where key and value are separated by a colon (:).
    - invoice_section_name -- The ID that uniquely identifies an invoice section.
    - profile_name -- The ID that uniquely identifies a billing profile.
    '''
    return _call_az("az billing product list", locals())


def show(account_name, name):
    '''
    Get a product by ID. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a product.
    '''
    return _call_az("az billing product show", locals())


def update(account_name, name, auto_renew=None, billing_frequency=None, status=None):
    '''
    Update the properties of a Product. Currently, auto renew can be updated. The operation is supported only for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a product.

    Optional Parameters:
    - auto_renew -- Indicates whether auto renewal is turned on or off for a product.
    - billing_frequency -- The frequency at which the product will be billed.
    - status -- The current status of the product.
    '''
    return _call_az("az billing product update", locals())


def move(account_name, name, destination_invoice_section_id=None):
    '''
    Moves a product's charges to a new invoice section. The new invoice section must belong to the same billing profile as the existing invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a product.

    Optional Parameters:
    - destination_invoice_section_id -- The destination invoice section id.
    '''
    return _call_az("az billing product move", locals())


def validate_move(account_name, name, destination_invoice_section_id=None):
    '''
    Validate if a product's charges can be moved to a new invoice section. This operation is supported only for products that are purchased with a recurring charge and for billing accounts with agreement type Microsoft Customer Agreement.

    Required Parameters:
    - account_name -- The ID that uniquely identifies a billing account.
    - name -- The ID that uniquely identifies a product.

    Optional Parameters:
    - destination_invoice_section_id -- The destination invoice section id.
    '''
    return _call_az("az billing product validate-move", locals())

