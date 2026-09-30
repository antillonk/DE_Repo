# Now we will join the pyspark tables together

# Our desired base grain for olist will be based on the order item level
# Orders may contain many items so this is our lowest business transaction grain
# All of our other tables are in the lowest transaction grain already

olist_sales_df = (
    olist_order_items_selected.alias("items")
    .join(olist_orders_selected.alias("orders"), on="order_id", how="left")
    .join(olist_customers_selected.alias("customers"), on="customer_id", how="left")
    .join(olist_products_selected.alias("products"), on="product_id", how="left")
    .join(olist_sellers_selected.alias("sellers"), on="seller_id", how="left")
    .join(review_summary.alias("review"), on="order_id", how="left")
    .join(payments_summary.alias("payments"), on="order_id", how= "left")
    .join(translations_selected.alias("translations"), on="product_category_name", how="left")
)

display(olist_sales_df.limit(100))
# Now we will join the pyspark tables together

