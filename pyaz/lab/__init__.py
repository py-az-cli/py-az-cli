from .. pyaz_utils import _call_az
from . import arm_template, artifact, artifact_source, custom_image, environment, formula, gallery_image, secret, vm, vnet


def get(name, resource_group, expand=None):
    return _call_az("az lab get", locals())


def delete(name, resource_group):
    return _call_az("az lab delete", locals())

