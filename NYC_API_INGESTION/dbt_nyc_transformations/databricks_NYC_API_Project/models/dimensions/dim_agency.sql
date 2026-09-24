{{ config(
    materialized='table',
    catalog='nyc_api_ingestion_project',
    schema='gold'
) }}

/*
ensure keys are unique to each unique value and exclude nulls
*/ 
with agencies as (

    select agency, agency_name
    from {{ ref('nyc_bronze') }}
    where agency is not null
    group by agency, agency_name

)

select
    {{ dbt_utils.generate_surrogate_key(['agency']) }}
        as agency_key

    , agency as agency_id
    , agency_name

from agencies