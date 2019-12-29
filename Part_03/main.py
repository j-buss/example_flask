import concurrent.futures

import flask
from google.cloud import bigquery

app = flask.Flask(__name__)
bigquery_client = bigquery.Client()


@app.route("/")
def main():
    query_job = bigquery_client.query(
    """
    SELECT
    FIPS_STATE.area_name as State_Name,
  FIPS_COUNTY.area_name as County_Name,
  Round(COUNTY_DATA.total_pop/1000000,2) AS Total_Population_Millions,
  ROUND(COUNTY_DATA.male_pop/1000000,2) AS Male_Population_Millions,
  ROUND(COUNTY_DATA.female_pop/1000000,2) AS Female_Population_Millions,
  COUNTY_DATA.median_age,
  SAFE_CAST(COUNTY_DATA.median_income AS INT64) As Median_Income
FROM 
  `bigquery-public-data.census_utility.fips_codes_all` AS FIPS_STATE
  INNER JOIN `bigquery-public-data.census_utility.fips_codes_all` AS FIPS_COUNTY
  ON FIPS_STATE.state = FIPS_COUNTY.state
  INNER JOIN `bigquery-public-data.census_bureau_acs.county_2017_5yr` AS COUNTY_DATA
  ON CONCAT(SAFE_CAST(FIPS_STATE.state AS String), SAFE_CAST(FIPS_COUNTY.county AS String)) = COUNTY_DATA.geo_id
WHERE
  FIPS_STATE.summary_level_name = 'state' and 
  FIPS_COUNTY.county is not NULL
ORDER BY
  total_pop desc
LIMIT 10
    """
    )
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
    project_id = flask.request.args.get("project_id")
    job_id = flask.request.args.get("job_id")
    location = flask.request.args.get("location")

    query_job = bigquery_client.get_job(
        job_id,
        project=project_id,
        location=location,
    )
    try:
        # Set a timeout because queries could take longer than one minute.
        results = query_job.result(timeout=30)
    except concurrent.futures.TimeoutError:
        return flask.render_template("timeout.html", job_id=query_job.job_id)

    return flask.render_template("query_result.html", results=results)


if __name__ == '__main__':
    app.run(host == "127.0.0.1", port=8080, debug=True)
