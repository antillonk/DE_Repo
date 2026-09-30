This folder was designed for a data engineering project utilizing databricks + spark 

This Folder location was created to display the following skills:

- API Ingestion leveraging python/pyspark in databricks
- Preserve original source data in a landing/raw layer
- Apply explicit schemas and ingestion metadata
- Standardize each company’s sales data independently
- Handle differences in identifiers, timestamps, currencies, and transaction grain
- Build a canonical conformed sales model
- Orchestrate the full workflow through Databricks Jobs
- Document architecture, assumptions, data contracts, and design decisions





To begin - 
1. I uploaded the CSV files for UCI and Olist using the csv upload wizard within the schema: ecommerce_de_project.stage.

2. Then I wanted more API practice, so I found another 2 data sets to import using python saving the file into my databricks workspace. For this I used PySpark Spark CSV reader. 
  2.1 refer to databricks_py_files folder for both sources/files

3.Now that all of my staging tables were set- I began using pyspark to clean the tables up
  3.1 source 1 came with a full data model, so I had to denormalize this table for merging purposes
  3.2 source 2 and 3 were both 1 single table so we only had to include the warehouse audit columns
  3.3 I created a data contract to ensure all tables can be unioned appropriately
  3.4 I noticed i had issues with the column names matching data contract so i went back to ensure each source table had a column matching the data contract
  3.5 merge successful - wrote the resulting dataframe as a delta table in the silver layer schema 
(refer to folder: databricks_notebooks / 01-07 _sales_silver_clean_merge.py -> these are the individual cells in the notebook I made for this pipeline)




