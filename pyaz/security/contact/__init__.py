from ... pyaz_utils import call_az

def list(**kwargs):
    '''
    List security contact.
    '''
    return call_az("az security contact list", locals())


def show(name, **kwargs):
    '''
    Shows a security contact.
    '''
    return call_az("az security contact show", locals())


def create(email, name, alert_notifications=None, alerts_admins=None, phone=None, **kwargs):
    '''
    Creates a security contact.
    '''
    return call_az("az security contact create", locals())


def delete(name, **kwargs):
    '''
    Deletes a security contact.
    '''
    return call_az("az security contact delete", locals())

