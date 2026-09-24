{{ config(
    materialized='table',
    database='nyc_api_ingestion_project',
    schema='gold'
) }}

/*
ensure keys are unique to each unique value and exclude nulls
*/ 
with location_types as (

    select UPPER(location_type) as location_type
    from {{ ref('nyc_bronze') }}
    where location_type is not null
    group by location_type

)

select
    {{ dbt_utils.generate_surrogate_key(['location_type']) }}
        as location_type_key,

    location_type

from location_types