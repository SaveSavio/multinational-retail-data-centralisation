
# import the DatabaseConnector class
# it serves for connecting and uploading data from various sources
from database_utils import DatabaseConnector as dbc

# this is the file with the credentials to connect the RDS AWS server
file_name = 'db_creds.yaml'

# reads credential and transform them from yaml to dict
cred_dict = dbc.read_db_creds(file_name)
print(cred_dict)

# initia
# lize the SQLalchemy engine with the provided credentials
RDS_engine = dbc.init_db_engine(cred_dict)

# import the DataExtractor class
# it has methods to read and extract data from various sources
from data_extraction import DataExtractor as de
# get the list of tables in the RDS database
tables_list = de.list_db_tables(RDS_engine)
# prints the list of tables
print(tables_list)

# reads the data from the RDS table of users
users_data = de.read_RDS_table(tables_list[1], RDS_engine)

# import the data cleaning Class
from data_cleaning import DataCleaning as dc

# the method clean_user_data cleans the data by means of pandas
user_data_clean = dc.clean_user_data(users_data)
 
#now upload the user data to the server
dbc.upload_to_db(user_data_clean, 'dim_users')
#print(df)

print(user_data_clean)

# extract all data from the following like
pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'
card_data = de.retrieve_pdf_data(pdf_link)
# print the data as they were extracted
print(card_data)
# clean the data through the relative method
card_data_clean = dc.clean_card_data(card_data)
# print the clean data
print(card_data_clean)

dbc.upload_to_db(card_data_clean, 'card_data_clean')

key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

number_of_stores = de.list_number_of_stores(url, key)
print(number_of_stores)


base_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'

stores_df = de.retrieve_stores_data(base_url, number_of_stores, key)

print(stores_df)
#stores_df.to_csv('stores_data.csv')

stores_data_clean = dc.clean_store_data(stores_df)

dbc.upload_to_db(stores_data_clean, 'dim_store_details')
