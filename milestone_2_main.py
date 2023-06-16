"""
    main.py
It serves as the entry point of the project Milestone 2 and contains the code to initialize and coordinate
the execution of other modules or classes.

It call methods that
    Connect to source and download data
    Clean the data
    Upload the data to a Postgresql database on localhost named sales_data

Those methods are contained in three classes coded in the files
    DatabaseConnector ---> database_utils
    DataCleaning --> data_cleaning.py
    DataExtractor --> data_extraction.py
    
"""
# import the DatabaseConnector class for connecting and uploading data from various sources
from database_utils import DatabaseConnector as dbc
# import the data cleaning Class
from data_cleaning import DataCleaning as dc
# import the DataExtractor class
from data_extraction import DataExtractor as de

"""
User data
"""

# the credentials to connect the RDS AWS server are stored in this yaml file
file_name = 'db_creds.yaml'

# read credential and transform them from yaml to dict
cred_dict = dbc.read_db_creds(file_name)

# initialize the SQLalchemy engine
RDS_engine = dbc.init_db_engine(cred_dict)

# get the list of tables in the RDS database
tables_list = de.list_db_tables(RDS_engine)

# print the list of tables
print(tables_list)

# read the data from the RDS table of users and stores in the users_data variable
users_data = de.read_RDS_table(tables_list[1], RDS_engine)


# clean the user data via the relative method
user_data_clean = dc.clean_user_data(users_data)

file_name_psql = 'db_creds.yaml'
cred_dict = dbc.read_db_creds(file_name_psql)

# upload the user data to the SQL server
dbc.upload_to_db(user_data_clean, 'dim_users', cred_dict_psql)

"""
Card data
"""
# extract the card data
pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
card_data = de.retrieve_pdf_data(pdf_link)

# clean the data through the relative method
card_data_clean = dc.clean_card_data(card_data)

# upload the card data to the SQL server
dbc.upload_to_db(card_data_clean, 'dim_card_details')

"""
Stores data
"""
# key and url to access the number of stores 
key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

# retrieve the number of stores
number_of_stores = de.list_number_of_stores(url, key)

# print the number of stores
print("the number of stores to be extracted is: ", number_of_stores)

# url for the stores information
base_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'

# download the information for each store
stores_df = de.retrieve_stores_data(base_url, number_of_stores, key)

# clean the stores data
stores_data_clean = dc.clean_store_data(stores_df)

# upload the stores data to the SQL database
dbc.upload_to_db(stores_data_clean, 'dim_store_details')

"""
Product data data
"""
# log into AWS CLI with (i) Access Key ID and (ii) Secret Access Key
import subprocess

# Pause script execution
input("Press Enter to pause the script and log in to AWC CLI")

# Log into AWS CLI
subprocess.call(["aws", "configure"])

# extract the products data from the s3 server
products_df = de.extract_from_s3('s3://data-handling-public/', filename = 'products.csv')

# clean the data
products_df_clean = dc.clean_product_data(products_df)
products_df_clean_converted_units = dc.clean_product_weights(products_df_clean)

# upload to the SQL server
dbc.upload_to_db(products_df_clean_converted_units, 'dim_products')

"""
Orders data
"""
orders_data = de.read_RDS_table(tables_list[2], RDS_engine)
orders_data_clean = dc.clean_orders_data(orders_data)

dbc.upload_to_db(orders_data_clean, 'orders_table')

url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
date_details = de.download_date_details(url)
print('date_details_downloaded')
date_details_clean = dc.clean_date_details(date_details)

dbc.upload_to_db(date_details_clean, 'dim_date_times')
