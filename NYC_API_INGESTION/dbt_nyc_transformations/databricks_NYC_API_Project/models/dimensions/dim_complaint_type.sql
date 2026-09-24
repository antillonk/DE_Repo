{{ config(
    materialized='table',
    database='nyc_api_ingestion_project',
    schema='gold'
) }}

/*
ensure keys are unique to each unique value and exclude nulls
*/ 
with complaint_types as (

    select UPPER(descriptor) as complaint_type
    from {{ ref('nyc_bronze') }}
    where descriptor is not null
    group by descriptor

)

select
    {{ dbt_utils.generate_surrogate_key(['complaint_type']) }}
        as complaint_type_key,

    complaint_type

from complaint_types