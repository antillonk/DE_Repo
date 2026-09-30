# Actions for union 

# create the data contract -> every table must contain the following columns

canonical_columns = [
    "source_system",
    "source_order_id",
    "source_order_item_id",
    "transaction_timestamp",
    "transaction_date",
    "source_customer_id",
    "source_product_id",
    "quantity",
    "unit_price_local",
    "country",
    "currency_code",
    "order_status",
    "ingest_dttm"
    # "dwh_processed_dttm"
]

# had to go back to ensure each table contains these columns in some way

# Now each tables DOES include the required columns

# Select ONLY the columns required for the contract of each table
olist_final = silver_olist_sales_df.select(canonical_columns)
uci_final = silver_uci_sales_df.select(canonical_columns)
superstore_final = silver_kaggle_sales_df.select(canonical_columns)


# Finally!! We can union and review
conformed_sales = (
    olist_final
    .unionByName(uci_final)
    .unionByName(superstore_final)
).withColumn("dwh_processed_dttm",F.current_timestamp())



# Beautiful we now have 1 single table conforming to our data contract AND we can now write this as a delta table
display(conformed_sales.limit(10000))



# write to delta table      *********
conformed_sales.write.format("delta").mode("overwrite").saveAsTable("ecommerce_de_project.silver.conformed_sales")

