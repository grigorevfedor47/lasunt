def submit_job(project_id, region, job_name, model_name, input_uri, output_uri):
    """Submits a batch prediction job to AI Platform.

    Args:
        project_id: project ID or project number of the Cloud project your job belongs to.
        region: region name.
        job_name: the name of the job that will be created.
        model_name: the name of the model that will serve the job.
        input_uri: the Cloud Storage URI of the input data.
        output_uri: the Cloud Storage URI of the output directory where the results will be stored.
    """

    from google.cloud import aiplatform

    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": "{}-aiplatform.googleapis.com".format(region)}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.JobServiceClient(client_options=client_options)
    model_parameters_dict = {}
    model_parameters = json.dumps(model_parameters_dict)
    batch_prediction_job = {
        "display_name": job_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model_name,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": "jsonl",
            "gcs_source": {"uris": [input_uri]},
        },
        "output_config": {
            "predictions_format": "jsonl",
            "gcs_destination": {"output_uri_prefix": output_uri},
        },
    }
    parent = f"projects/{project_id}/locations/{region}"
    response = client.create_batch_prediction_job(
        parent=parent, batch_prediction_job=batch_prediction_job
    )
    print("response:", response)

  
