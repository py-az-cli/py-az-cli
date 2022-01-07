from ... pyaz_utils import _call_az

def query_by_pipeline_run(last_updated_after, last_updated_before, name, run_id, workspace_name, continuation_token=None, filters=None, order_by=None):
    '''
    Query activity runs based on input filter conditions.

    Required Parameters:
    - last_updated_after -- The time at or after which the run event was updated in 'ISO 8601' format.
    - last_updated_before -- The time at or before which the run event was updated in 'ISO 8601' format.
    - name -- The pipeline name.
    - run_id -- The pipeline run identifier.
    - workspace_name -- The workspace name.

    Optional Parameters:
    - continuation_token -- The continuation token for getting the next page of results. Null for first page.
    - filters -- List of filters.
    - order_by -- List of OrderBy option.
    '''
    return _call_az("az synapse activity-run query-by-pipeline-run", locals())

