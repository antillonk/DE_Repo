# Now we will add our derived columns for the enterprise model
# keep original desired dataframe and add standard columns to dataframe for silver layer

silver_olist_sales_df = (
    olist_sales_df
    .withColumn(
        "source_order_id",
        F.col("order_id")                                           #to match the data contract
    )
    .withColumn(
        "source_customer_id",
        F.col("customer_id")                                        #to match the data contract
    )
    .withColumn(
        "source_product_id",
        F.col("product_id")                                         #to match the data contract
    )
    .withColumn(
        "quantity",
        F.lit(1)                                                  #later on we see that another data set includes qty - we must preserve the grain so we will assume all
                                            #qty = 1
    )
    .withColumn(
        "country",
        F.lit("Brazil")                                             # We must identify the country for future dataset differentiation
    )
    .withColumn(
        "transaction_timestamp",
        F.to_timestamp("order_purchase_timestamp")                  #exact timestamp
    )
    .withColumn(
        "order_delivered_customer_date",
        F.to_timestamp("order_delivered_customer_date")
    )
    .withColumn(
        "order_estimated_delivery_date",
        F.to_timestamp("order_estimated_delivery_date")
    )
    .withColumn(
        "transaction_date",
        F.to_date("order_purchase_timestamp")                       #only date of order
    )
    .withColumn(
        "unit_price_local",
        F.col("price").cast("decimal(18,2)")
    )
    .withColumn(
        "shipping_amount",
        F.col("freight_value").cast("decimal(18,2)")
    )
    .withColumn(
        "total_item_amount",
        F.col("unit_price_local") + F.col("shipping_amount")
    )
    .withColumn(
        "currency_code",
        F.lit("BRL")                                                # Brazilian Real hardcoded as this is the only currency
    )
    .withColumn(
        "source_system",
        F.lit("company_a_olist")                                    #source system hardcoded
    )
    # .withColumn(
    #     "ingest_dttm",
    #     F.current_timestamp()
    # )
    .withColumn(
        "is_delivered_late",
        F.when(
            F.col("order_delivered_customer_date")
            > F.col("order_estimated_delivery_date"),
            True
        ).otherwise(False)
    )
)

display(silver_olist_sales_df.limit(1000))
