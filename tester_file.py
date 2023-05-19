
# import the DatabaseConnector class
# it serves for connecting and uploading data from various sources
from database_utils import DatabaseConnector as dbc

# this is the file with the credentials to connect the RDS AWS server
file_name = 'db_creds.yaml'

# reads credential and transform them from yaml to dict
cred_dict = dbc.read_db_creds(file_name)
print(cred_dict)

# initialize the SQLalchemy engine with the provided credentials
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
clean_user_data = dc.clean_user_data(users_data)

#now upload the user data to the server
dbc.upload_to_db(clean_user_data, 'dim_users')
#print(df)

print(clean_user_data)

# extract all data from the following like
pdf_link = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf'

pdf_data = de.retrieve_pdf_data(pdf_link)

print(pdf_data)