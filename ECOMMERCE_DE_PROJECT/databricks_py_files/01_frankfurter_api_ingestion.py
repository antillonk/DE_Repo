import requests
from pyspark.sql.types import StructType, StructField, StringType, DoubleType

URL = 'https://api.frankfurter.dev/v2/rates?base=usd'

response = requests.get(URL)
response.raise_for_status()
records = response.json() 


schema = StructType([
    StructField('date', StringType(), True),
    StructField('base', StringType(), True),
    StructField('quote', StringType(), True),
    StructField('rate', StringType(), True)
])

rates_df = spark.createDataFrame(records, schema=schema)


# validating the schema/data types
# display(rates_df)

# write the delta table
rates_df.write.format("delta").mode("append").saveAsTable("ecommerce_de_project.stage.frankfurter_api_exchange_rate")


# verify delta table from desired schema
spark.sql(f"""
    SELECT
        *
    FROM {"ecommerce_de_project.stage.frankfurter_api_exchange_rate"}
""").show()

# verified  *****
