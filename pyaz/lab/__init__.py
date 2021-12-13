from .. pyaz_utils import call_az
from . import arm_template, artifact, artifact_source, custom_image, environment, formula, gallery_image, secret, vm, vnet


def get(name, resource_group, expand=None, **kwargs):
    return call_az("az lab get", locals())


def delete(name, resource_group, **kwargs):
    return call_az("az lab delete", locals())

