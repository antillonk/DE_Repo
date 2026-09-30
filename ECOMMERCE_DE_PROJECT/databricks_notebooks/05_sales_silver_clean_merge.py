# Begin process with source 2

# select table/columns - no joins needed for this data set so we will match the source systems column profile the best we can 
uci_sales_df = uci_sales.select(
    F.col("invoice").cast("string").alias("source_invoice_id"), # we will add order_id using this value
    F.col("stockcode").cast("string").alias("source_stockcode_id"), # we will use this as product_id 
    F.col("description"), # not in source
    F.col("quantity").cast("integer"),
    F.to_timestamp("invoicedate", "MM-dd-yyyy HH:mm:ss").alias("source_invoice_date"), #we will use this as order purchase date
    F.col("price").cast("decimal(18,2)").alias("price"),
    F.col("customer_id").cast("string").alias("source_customer_id"), # we will use this as customer_id
    F.col("country").cast("string").alias("country"), # we will have to model the other tables to include country
    F.col("INGEST_DTTM").cast("timestamp").alias("ingest_dttm")
)



silver_uci_sales_df = (
    uci_sales_df
    .withColumn(
        "transaction_timestamp",
        F.to_timestamp("source_invoice_date")               # We will assume the business uses invoice date as order purchase date for this project
    )
    .withColumn(
        "source_order_id",
        F.col("source_invoice_id")                         #For data contract
    )
    .withColumn(
        "source_order_item_id",
        F.lit(None)                                         #does not exist
    )
    .withColumn(
        "transaction_date",
        F.to_date("source_invoice_date")                    #only date of order
    )
    .withColumn(
        "unit_price_local",
        F.col("price").cast("decimal(18,2)")
    )
    .withColumn(
        "source_product_Id",
        F.col("source_stockcode_id")                        #stock code will serve as product id
    )
    .withColumn(
        "total_item_amount",
        F.col("price") 
        # + F.col("shipping_amount")                        #does not exist
    )
    .withColumn(
        "currency_code",
        F.lit("GBP")                                        # Great Britain Pound hardcoded as this is the only currency
    )
    .withColumn(
        "source_system",
        F.lit("company_b_uci")                              #source system hardcoded
    )
    # .withColumn(
    #     "ingest_dttm",
    #     F.current_timestamp()
    # )
    .withColumn(
        "is_delivered_late",
        F.lit(False)                                        #does not exist, therefore, the assumption will be all deliveries are on-time
    )
    .withColumn(
        "order_status",
        F.lit("delivered")                                  #does not exist, therefore, the assumption will be all deliveries have been completed
    )
)



display(silver_uci_sales_df.limit(1000))
