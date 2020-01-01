import flask

from google.cloud import bigquery
bigquery_client = bigquery.Client()

app = flask.Flask(__name__)

@app.route("/")
def main():
    # Define query_job and query object
    query_job = bigquery_client.query(
        """
        SELECT 
          COUNT(*) as Rec_Count 
        FROM 
          `bigquery-public-data.census_utility.fips_codes_all`
        """
    )
    # Redirect to the Results function below
    return flask.redirect(
        flask.url_for(
            "results",
            project_id=query_job.project,
            job_id=query_job.job_id,
            location=query_job.location,
        )
    )

@app.route("/results")
def results():
    # Get the Arguments that were passed into the url
    project_id = flask.request.args.get("project_id")
    job_id = flask.request.args.get("job_id")
    location = flask.request.args.get("location")

    # Get the BigQuery Job using the Arguments passed into the url
    query_job = bigquery_client.get_job(
        job_id,
        project=project_id,
        location=location,
    )

    # Try to get the results from the query;
    #   Display the results in the query result template
    # Else if the exception TimeoutError then show the timeout page
    try:
        # Set a timeout because queries could take longer than one minute.
        results = query_job.result(timeout=30)
    except concurrent.futures.TimeoutError:
        return flask.render_template("timeout.html", job_id=query_job.job_id)

    return flask.render_template("query_result.html", results=results)

if __name__ == "__main__":
    app.run(port=8080)
