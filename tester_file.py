
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
# now let's move these data to a Jupyter notebook to define the cleaning functions interactively

users_data.to_csv('RDS_table.csv')

from data_cleaning import DataCleaning as dc
clean_user_data = dc.clean_user_data(users_data)

#now upload the user data to the server
df = dbc.upload_to_db(clean_user_data, 'dim_users', engine)
print(df)
#%%
print(users_data)
# %%
