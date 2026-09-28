This folder was designed for a data engineering project utilizing databricks + spark 

Primary objectives:
  Ingest multiple source files using PySpark.
  Preserve original source data in a landing/raw layer.
  Create source-specific Bronze Delta tables.
  Apply explicit schemas and ingestion metadata.
  Standardize each company’s sales data independently.
  Handle differences in identifiers, timestamps, currencies, and transaction grain.
  Deduplicate records and isolate invalid data.
  Create customer and product crosswalks.
  Build a canonical conformed sales model.
  Support incremental processing and safe reruns.
  Track pipeline metrics and data-quality results.
  Orchestrate the full workflow through Databricks Jobs.
  Document architecture, assumptions, data contracts, and design decisions.



To begin - 
I uploaded the CSV files for UCI and Olist using the csv upload wizard within the schema: ecommerce_de_project.stage.

Then I wanted more API practice, so I found another data set to import. For this I used PySpark Spark CSV reader. 

Now I have all sources ready in stage (bronze layer) 

