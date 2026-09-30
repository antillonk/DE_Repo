# Begin process with source 3

# select table/columns - no joins needed for this data set so we will match the source systems column profile the best we can 
kaggle_sales = kaggle_sales.select(
    F.col("row_id").cast("string").alias("source_row_id"), # preserve source
    F.col("order_id").cast("string").alias("source_order_id"), # we will add order_id using this value
    F.col("order_date").cast("date").alias("source_order_date"), # we will use this as order purchase date
    F.col("ship_date").cast("date").alias("source_ship_date"), # we will use this as order purchase date
    F.col("ship_mode").cast("string").alias("source_ship_mode"), # not in current model
    F.col("customer_id").cast("string").alias("source_customer_id"), # we will use this as customer_id
    F.col("customer_name").cast("string").alias("source_customer_name"), # not in current model
    F.col("segment").cast("string").alias("source_segment"), # not in current model
    F.col("country").cast("string"),
    F.col("city").cast("string").alias("customer_city"), # not in current model
    F.col("state").cast("string").alias("customer_state"), # not in current model
    F.col("postal_code").cast("string").alias("customer_postal_code"), # not in current model
    F.col("region").cast("string").alias("customer_region"), # not in current model
    F.col("product_id").cast("string").alias("source_product_id"), # we will use this as product_id
    F.col("category").cast("string").alias("category"), # this will be category
    F.col("sub_category").cast("string").alias("sub_category"),
    F.col("product_name").cast("string").alias("product_name"),
    F.col("sales").cast("string").alias("source_sales"),
    F.col("quantity").cast("decimal(18,2)").alias("quantity"),
    F.col("discount").cast("decimal(18,2)").alias("discount"),
    F.col("profit").cast("decimal(18,2)").alias("profit"),
    F.col("ingest_dttm").cast("timestamp").alias("ingest_dttm")   
)


silver_kaggle_sales_df = (
    kaggle_sales
    .withColumn(
        "transaction_timestamp",
    F.to_timestamp("source_order_date")                                     # No time associated but we need to match the data contract 
    )
    .withColumn(
        "source_order_item_id",
        F.lit(None)                                                          # no line items associated but we need to match the data contract 
    )
    .withColumn(
        "transaction_date",
        F.to_date("source_order_date")                                      #only date of order
    )
    .withColumn(
        "unit_price_local",
        F.col("source_sales").cast("decimal(18,2)")
    )
    .withColumn(
        "total_item_amount",
        F.col("source_sales") 
    # + F.col("shipping_amount")                                            #does not exist
    )
    .withColumn(
        "currency_code",
    F.lit("USD")                                                            # US dollar hardcoded as this is the only currency
    )
    .withColumn(
        "source_system",
        F.lit("company_c_kaggle_superstore")                                #source system hardcoded
    )
    # .withColumn(
    #     "ingest_dttm",
    #     F.current_timestamp()
    # )
    .withColumn(
        "order_status",
        F.lit("delivered")                                                  #does not exist, therefore, the assumption will be all deliveries have been completed
    )
)



display(silver_kaggle_sales_df.limit(1000))
