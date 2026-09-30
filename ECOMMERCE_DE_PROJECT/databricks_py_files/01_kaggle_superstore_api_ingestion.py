# Enable Kaggle for import in this kernel in this notebook *********
# %pip install kagglehub
# %restart_python
# End                                                      *********

# import kagglehub #only needed for first time download - we will revisit this process to create an ingestion pipeline
import os
from pyspark.sql import functions as F


# # download API file to local workspace due to free Databricks license conflict *********
workspace_download_path = (
    "/Workspace/Users/antillonk@gmail.com/kaggle_downloads/superstore"
)

# # download to this newly created path *********
# dataset_path = kagglehub.dataset_download(
#     "ishanshrivastava28/superstore-sales",
#     output_dir=workspace_download_path,
#     force_download=True
# )

# # Test if the file successfully downloaded    *********
# print(dataset_path)
# print(os.listdir(dataset_path))


# Download successful ******* 
# The nice thing about this path is that we can do this in enterprise if we have a shared workspace with the DE group

# continue from here    *********


# Verify file download. 
superstore_df = (
    spark.read
    .format("csv")
    .option("header", "true")
    .option("inferSchema", "true")
    # had some issues with commas and quotes creating ingest issues - testing additional options
    # These issues were found at the transformation stage when casting columns
    .option("quote", '"')
    .option("escape", '"')
    .option("mode", "PERMISSIVE")
    .option("columnNameOfCorruptRecord", "_corrupt_record")
    # 
    .csv(f"{workspace_download_path}/Superstore.csv") #had to add the "/" here since the original path was the initial creation
)


# ****PySpark and Pandas dataframes are different***
# Pandas DF's = mutable
# PySpark DF's <> mutable

# Does not work -- NOT PANDAS
# for i in superstore_df.columns:
#     superstore_df = superstore_df.withColumnRenamed(i, i.replace(" ", "_"))
#     superstore_df = superstore_df.withColumnRenamed(i, i.upper())


remove_space_superstore_df = superstore_df.select(
    [
        F.col(c).alias(c.replace(' ', '_')) 
        for c in superstore_df.columns
     ])

upper_superstore_df = remove_space_superstore_df.select(
    [
        F.col(c).alias(c.upper()) 
        for c in remove_space_superstore_df.columns
    ])

superstore_df_new = upper_superstore_df

# Need a timestamp to determine when I loaded this in
superstore_df_new = upper_superstore_df.withColumn("ingest_dttm", F.current_timestamp())

# Check Results
# display(superstore_df_new.limit(10))
# superstore_df.printSchema()

# verfied *********

# write to delta table      *********
superstore_df_new.write.format("delta").mode("overwrite").saveAsTable("ecommerce_de_project.stage.kaggle_api_from_pyfile_superstore")

# verify within a sql notebook
# query verified: SELECT * FROM ecommerce_de_project.stage.kaggle_api_from_pyfile_superstore;
