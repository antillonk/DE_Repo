{{ config(
    materialized='table',
    database='nyc_api_ingestion_project',
    schema='gold'
) }}


SELECT 
    T1.complaint_id
    ,T3.agency_key
    ,T2.complaint_type_key
    ,T4.location_type_key
    ,T1.address
    ,T1.city
    ,T1.borough
    ,T1.zip
    ,current_timestamp() as ingest_dttm
FROM {{ ref('nyc_silver_fact') }} T1
LEFT JOIN {{ ref('dim_complaint_type') }} T2
    ON T1.complaint_type = T2.complaint_type
LEFT JOIN {{ ref('dim_agency') }} T3 
    ON T1.agency_id = T3.agency_id
LEFT JOIN {{ ref('dim_location_type') }} T4 
    ON T1.location_type = T4.location_type
