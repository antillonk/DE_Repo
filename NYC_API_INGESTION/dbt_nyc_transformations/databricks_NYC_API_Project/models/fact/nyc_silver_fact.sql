{{ config(
    materialized='view',
    database='nyc_api_ingestion_project',
    schema='silver'
) }}


select 
    CAST(unique_key as bigint) AS complaint_id
    ,CAST(created_date as timestamp) AS complaint_submitted_dttm
    ,agency AS agency_id
    -- ,agency_name -- I will save this for the dimension table and keep only the id here
    ,UPPER(descriptor) as complaint_type
    ,coalesce(UPPER(location_type), '**NOT SPECIFIED') as location_type
    --The columns below will not contain keys
    ,coalesce(UPPER(incident_address), '**NOT SPECIFIED') as address
    ,coalesce(city, '**NOT SPECIFIED') as city
    ,borough
    ,incident_zip as zip
    -- ,park_borough -- in our dataset, there no occurence where borough <> park_borough
    ,current_timestamp() as ingest_dttm
from {{ source('nyc_api_source_data', 'nyc_api_service_request') }}
WHERE unique_key IS NOT NULL

