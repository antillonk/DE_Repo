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
I uploaded the CSV files for UCI and Olist using the csv upload wizard within the schema: ecommerce_de_project.stage.

Then I wanted more API practice, so I found another data set to import. For this I used PySpark Spark CSV reader. 

Now I have all sources ready in stage (bronze layer) 

