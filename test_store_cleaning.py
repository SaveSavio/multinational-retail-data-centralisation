
#%%
from data_extraction import DataExtractor as de
key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

number_of_stores = de.list_number_of_stores(url, key)
print(number_of_stores)


base_url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/'

stores_df = de.retrieve_stores_data(base_url, number_of_stores, key)

print(stores_df)

#%%
import pandas as pd

df = stores_df
# remove any column with all NaN
df = df[df.notna().any(axis=1)]
# remove all the columns with strange lat
df = df[~df['lat'].notnull()]
# drop specific rows with NaN
df.loc[215:220]
#df.drop([217, 405, 437], axis = 0, inplace = True)
df = df[~df['country_code'].isna()]

df.drop(columns = ['lat', 'index'], inplace = True)
df['latitude'] = df['latitude'].astype(float).abs()

import datetime
df['opening_date'] = pd.to_datetime(df['opening_date'], infer_datetime_format=True, errors = 'coerce')
staff_mask = df['staff_numbers'].apply(pd.to_numeric, errors='coerce').isnull()

import numpy as np
mean_staff = df['staff_numbers'][staff_mask == False].astype(int).mean()

df.loc[staff_mask == True, 'staff_numbers'] = mean_staff

# %%
print(len(df))
# %%
