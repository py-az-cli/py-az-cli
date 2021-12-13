from .... pyaz_utils import call_az

def list(dps_name, resource_group, **kwargs):
    '''
    List all certificates contained within an Azure IoT Hub device provisioning service
    '''
    return call_az("az iot dps certificate list", locals())


def show(certificate_name, dps_name, resource_group, **kwargs):
    '''
    Show information about a particular Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate show", locals())


def create(certificate_name, dps_name, path, resource_group, verified=None, **kwargs):
    '''
    Create/upload an Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate create", locals())


def delete(certificate_name, dps_name, etag, resource_group, **kwargs):
    '''
    Delete an Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate delete", locals())


def generate_verification_code(certificate_name, dps_name, etag, resource_group, **kwargs):
    '''
    Generate a verification code for an Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate generate-verification-code", locals())


def verify(certificate_name, dps_name, etag, path, resource_group, **kwargs):
    '''
    Verify an Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate verify", locals())


def update(certificate_name, dps_name, etag, path, resource_group, verified=None, **kwargs):
    '''
    Update an Azure IoT Hub Device Provisioning Service certificate.
    '''
    return call_az("az iot dps certificate update", locals())

