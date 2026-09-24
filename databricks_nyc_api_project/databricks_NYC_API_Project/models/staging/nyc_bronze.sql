{{ config(materialized='table') }}


select *
from  {{ source('nyc_api_source_data', 'nyc_api_service_request') }}