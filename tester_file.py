from database_utils import DatabaseConnector as dbc
file_name = 'db_creds.yaml'

# read credential and transform them from yaml to dict
cred_dict = dbc.read_db_creds(file_name)
#print(cred_dict)
#print(type(cred_dict))

# initialize engine
dbc.init_db_engine(cred_dict)
