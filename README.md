# DE_Repo
Data/Analytics Engineering Portfolio


1. To begin - I tested api ingestion first:
    NYC_API_INGESTION / databricks_py_files / 01_ingest_nyc311_bronze_verification.py

2. Then I had a stage delta table inside of my desired schema in databricks. 

3. Now moving on to DBT + data modeling + transformation: 
  
   3.1. I began with the stage table for reference: 
          databricks_NYC_API_Project / models / staging / nyc_bronze.sql
  
   3.2 Next I began to work on cleaning the base table to be easier to read and clear any possible inconsistencies in the data
          databricks_NYC_API_Project / models / fact / nyc_silver_fact.sql

  3.3 Now dimensions can be created for a proper star schema data model (anything that realistically CAN be an attribute table) where I apply the surrogate keys
          databricks_NYC_API_Project / models / dimensions / dim_agency.sql
          databricks_NYC_API_Project / models / dimensions / dim_complaint_type.sql
          databricks_NYC_API_Project / models / dimensions / dim_location_type.sql

  3.4 From here, I return for the gold fact. Strip out the attributes and join in the dimension surrogate keys for easy downstream ready analytics 
          databricks_NYC_API_Project / models / fact / nyc_gold_fact.sql


4. Run the dbt commands to clean / build the model within databricks:
    *within my project path* > dbt clean
    *within my project path* > dbt build --select +nyc_gold_fact

5. verify the materialization of the model within databricks

6. clean up any issues that may have been flagged

7. Not completed within this project, however, here I would get with an SME and get as much context as possible to submit into the .yaml file for an AI ready model
    (think, column names, descriptions, reasons for keeping columns, synonyms, relationships, explanation of various date columns, etc...) 

8. In this step, I productionized the ingestion as a notebook- note: I noticed that I needed a helper function that can be re-used for another project of this type - kept that separate for modularity.
       NYC_API_INGESTION / databricks_py_files / 02_ingest_nyc311_bronze_job.py

9. Within databricks - I created a job that runs the notebook: 02_ingest_nyc311_bronze_job.py on schedule.

10. Now this this is an append job with batch run info - the silver layer must be modified to handle duplicate records.
11. 
