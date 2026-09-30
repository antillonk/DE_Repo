import sys
from pyspark.sql import functions as F
from pyspark.sql.functions import desc , col, lit, udf, sum, count, avg, max, min, countDistinct, explode, array, struct

# Hard-code location 
func_path = "/Workspace/Users/antillonk@gmail.com/modular_functions"

if func_path not in sys.path:
    sys.path.append(func_path)

# Modular functions
import mod_functions

olist_orders = spark.table("ecommerce_de_project.stage.olist_orders_dataset")
# verify pattern first: 
# display(olist_orders.limit(10))

# initiate spark tables
olist_order_items = spark.table("ecommerce_de_project.stage.olist_order_items_dataset")
olist_customers = spark.table("ecommerce_de_project.stage.olist_customers_dataset")
olist_products = spark.table("ecommerce_de_project.stage.olist_products_dataset")
olist_sellers = spark.table("ecommerce_de_project.stage.olist_sellers_dataset")
olist_payments = spark.table("ecommerce_de_project.stage.olist_order_payments_dataset")
olist_reviews = spark.table("ecommerce_de_project.stage.olist_order_reviews_dataset")
olist_translation = spark.table("ecommerce_de_project.stage.olist_product_category_name_translation")
uci_sales = spark.table("ecommerce_de_project.stage.uci_sales")
kaggle_sales = spark.table("ecommerce_de_project.stage.kaggle_api_from_pyfile_superstore")
forex_rates = spark.table("ecommerce_de_project.stage.frankfurter_api_exchange_rate")

# standardize column names for any tables that were imported using the csv wizard
# source 1
olist_orders = mod_functions.standardize_column_names(olist_orders) # contains general order data - customer, status, date ordered etc...
olist_order_items = mod_functions.standardize_column_names(olist_order_items) # contains what what is in each order, including cost by item sold
olist_customers = mod_functions.standardize_column_names(olist_customers) # contains customer data such as id and shipping address
olist_products = mod_functions.standardize_column_names(olist_products) # contains category and shipping information about each item sold
olist_sellers = mod_functions.standardize_column_names(olist_sellers) # contains seller data such as id and ship from address
olist_payments = mod_functions.standardize_column_names(olist_payments) # contains payment data such as payment type and value + installments
olist_reviews = mod_functions.standardize_column_names(olist_reviews) # contains review data such as score and comments
olist_translation = mod_functions.standardize_column_names(olist_translation) # contains product category translations from port. to eng.  
# source 2
uci_sales = mod_functions.standardize_column_names(uci_sales) # contains all pertinant sales data for UCI sales
# source 3
kaggle_sales = mod_functions.standardize_column_names(kaggle_sales) # contains all pertinant sales data for superstore sales 
# source 4
forex_rates = mod_functions.standardize_column_names(forex_rates) # Contains the daily exchange rates for the currencies for merging


# Used to understand the data 
display(forex_rates.limit(10000))
