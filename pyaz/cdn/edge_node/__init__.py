from ... pyaz_utils import call_az

def list(**kwargs):
    return call_az("az cdn edge-node list", locals())

