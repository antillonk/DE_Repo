# Now we will select the pyspark tables for joins

olist_orders_selected = olist_orders.select(
    "order_id",
    "customer_id",
    "order_status",
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
    "INGEST_DTTM"
)

olist_order_items_selected = olist_order_items.select(
    "order_id",
    F.col("order_item_id").cast("string").alias("source_order_item_id"),                           #returned to modify this to match the data contract
    "product_id",
    "seller_id",
    "shipping_limit_date",
    "price",
    "freight_value"
)

olist_customers_selected = olist_customers.select(
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state"
)

olist_products_selected = olist_products.select(
    "product_id",
    "product_category_name",
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
)

olist_sellers_selected = olist_sellers.select(
    "seller_id",
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state"
)

translations_selected = olist_translation.select(
    "product_category_name",
    "product_category_name_english"
)


# This will be joined to standardize to USD
forex_rates_selected = forex_rates.select(
    "date",
    "base",
    "quote",
    "rate"
)
