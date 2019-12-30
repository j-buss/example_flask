from flask import Flask

from google.cloud import bigquery
bigquery_client = bigquery.Client()

app = Flask(__name__)

def bq_query():
    query_job = bigquery_client.query(
        """
        SELECT 
          COUNT(*) as Rec_Count 
        FROM 
          `bigquery-public-data.census_utility.fips_codes_all`
        """
    )
    return query_job.result()

@app.route("/")
def main():
    res = bq_query()
    for row in res:
        output = "Record Count: " + str(row[0])
    return output

if __name__ == "__main__":
    app.run(port=8080)
