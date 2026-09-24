import requests
import time
import sys
import uuid
from datetime import datetime, timezone
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from delta.tables import DeltaTable

# Hard-code location 
func_path = "/Workspace/Users/antillonk@gmail.com/modular_functions"

if func_path not in sys.path:
    sys.path.append(func_path)

# Modular functions
import mod_functions


API_URL = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"

PAGE_SIZE = 5000
MAX_RECORDS = 20000

TABLE_NAME = "nyc311.bronze_service_requests"

# step 2
batch_id = str(uuid.uuid4())
ingested_at = datetime.now(timezone.utc)

all_records = []
offset = 0

while len(all_records) < MAX_RECORDS:
    remaining = MAX_RECORDS - len(all_records)
    request_size = min(PAGE_SIZE, remaining)

    page = mod_functions.get_api_page(
        API_URL = API_URL,
        offset=offset,
        limit=request_size
    )

    if not page:
        break

    all_records.extend(page)
    offset += len(page)

    print(f"Retrieved {len(all_records)} records")

    if len(page) < request_size:
        break


# Validate response

# if not all_records:
#     raise ValueError("The API returned no records.")

# required_columns = {"unique_key", "created_date"}

# missing_columns = required_columns - set(all_records[0].keys())

# if missing_columns:
#     raise ValueError(
#         f"API response is missing expected columns: {missing_columns}"
#     )

# print(f"Retrieved {len(all_records)} records in batch {batch_id}")

# END Validate response


# same schema issues as in file 01
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


# Now view results
raw_df = spark.createDataFrame(all_records, schema=schema)

bronze_df = (
    raw_df
    .withColumn("_batch_id", F.lit(batch_id))
    .withColumn("_ingested_at", F.lit(ingested_at))
    .withColumn("_source_url", F.lit(API_URL))
    .withColumn("_source_offset", F.monotonically_increasing_id())
)


# write as delta table - since we are adding additional columns for documentation -> new table 
bronze_df.write.format("delta").mode("append").saveAsTable("nyc_api_ingestion_project.bronze.nyc_api_service_request_02")

# verify delta table from desired schema
spark.sql(f"""
    SELECT
        COUNT(*) AS total_rows,
        COUNT(DISTINCT _batch_id) AS ingestion_batches,
        MIN(_ingested_at) AS first_ingestion,
        MAX(_ingested_at) AS latest_ingestion
    FROM {"nyc_api_ingestion_project.bronze.nyc_api_service_request_02"}
""").show()
