from database_utils import DatabaseConnector as dbc
file_name = 'db_creds.yaml'

# read credential and transform them from yaml to dict
cred_dict = dbc.read_db_creds(file_name)
#print(cred_dict)
#print(type(cred_dict))

# initialize engine
engine = dbc.init_db_engine(cred_dict)

from data_extraction import DataExtractor as de
tables_list = de.list_db_tables(engine)
print(tables_list)

users_data = de.read_RDS_table(tables_list[2], engine)

print(users_data)