{{ config(materialized='table') }}

-- updated due source due to productionized append ingestion for batch history
select *
-- from  {{ source('nyc_api_source_data', 'nyc_api_service_request') }}
from  {{ source('nyc_api_source_data', 'nyc_api_service_request_02') }}
