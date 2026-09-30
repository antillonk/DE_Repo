{{ config(
    materialized='table',
    catalog='nyc_api_ingestion_project',
    schema='gold'
) }}

/*
ensure keys are unique to each unique value and exclude nulls
*/ 
with agencies as (

    select agency_id, agency_name
    from {{ ref('nyc_silver_fact') }}
    where agency_id is not null
    group by agency_id, agency_name

)

select
    {{ dbt_utils.generate_surrogate_key(['agency_id']) }}
        as agency_key

    , agency_id
    , agency_name

from agencies
