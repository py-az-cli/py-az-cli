from ... pyaz_utils import call_az
from . import record_set, zone


def list_references(parameters, **kwargs):
    return call_az("az network dns list-references", locals())

