import requests
import pandas as pd
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Source
url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

# Parameters
params = {
            "$limit": 100000,
            "$order": "created_date DESC"
            # "$offset": 0,
        }

# Assign API call to a variable
response = requests.get(url, params=params)
response.raise_for_status()
records = response.json() 

# len(records), records[0]

# Lets review the raw data
# pd.set_option('display.max_columns', 50)
# raw_df =pd.DataFrame(records)
# print(raw_df)

# Issues with datatypes - explicitly define schema 
# Suprisingly enough, databricks actually knew the schema of the data for autofill...wow

schema = StructType([
    StructField("unique_key", StringType(), True), #unique key caused error with integer - had to modify to string
    StructField("created_date", StringType(), True),
    StructField("agency", StringType(), True),
    StructField("agency_name", StringType(), True),
    StructField("descriptor", StringType(), True),
    StructField("location_type", StringType(), True),
    StructField("incident_zip", StringType(), True),
    StructField("incident_address", StringType(), True),
    StructField("city", StringType(), True),
    StructField("borough", StringType(), True),
    StructField("x_coordinate_state_plane", StringType(), True),
    StructField("y_coordinate_state_plane", StringType(), True),
    StructField("park_facility_name", StringType(), True),
    StructField("park_borough", StringType(), True),
    StructField("latitude", StringType(), True),
    StructField("longitude", StringType(), True),
    StructField("location", StringType(), True)
])
    
# due to failure to infer the datatypes -> add the schema
raw_df_Spark = spark.createDataFrame(records, schema=schema)

# validating the schema/data types
# display(raw_df_Spark)
# raw_df_Spark.printSchema()

# write this as a table - Delta so we can update/delete/merge
# lets name the table with source_tablename
raw_df_Spark.write.format("delta").mode("append").saveAsTable("nyc_api_ingestion_project.bronze.nyc_api_service_request")





