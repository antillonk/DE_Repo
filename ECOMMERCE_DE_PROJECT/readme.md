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
