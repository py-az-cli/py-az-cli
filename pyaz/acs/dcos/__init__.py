from ... pyaz_utils import call_az

def browse(name, resource_group, disable_browser=None, ssh_key_file=None, **kwargs):
    return call_az("az acs dcos browse", locals())


def install_cli(client_version=None, install_location=None, **kwargs):
    '''
    Download and install the DC/OS command-line tool for a cluster.
    '''
    return call_az("az acs dcos install-cli", locals())

