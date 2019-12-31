import flask

from google.cloud import bigquery
bigquery_client = bigquery.Client()

app = flask.Flask(__name__)

@app.route("/")
def main():
    query_job = bigquery_client.query(
        """
        SELECT 
          COUNT(*) as Rec_Count 
        FROM 
          `bigquery-public-data.census_utility.fips_codes_all`
        """
    )
    return flask.render_template("query_result.html", results=query_job.result())

if __name__ == "__main__":
    app.run(port=8080)
