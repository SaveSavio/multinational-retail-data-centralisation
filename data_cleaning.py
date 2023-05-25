
class DataCleaning:
    """
    Defines methods to clean data the user data from various datasources.
    """
    def clean_user_data(df):
        
        """
        Performs the cleaning of the user data for NULL values, errors with dates, incorrectly
        typed values and rows filled with the wrong information.
            Parameters:
                A pandas dataframe
            Returns:
                The same dataframe, but cleaned.

        """
        import pandas as pd
        import datetime

        # drop the index columns, it is redundant
        df = df.drop(['index'], axis = 1)
        
        # drop the rows containing NaNs
        df = df[df.notna().any(axis=1)]

        # transform the DOE from string to a datetime object. The errors option will
        # set a NaT for every date that cannot be interpreted 
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], infer_datetime_format=True, errors = 'coerce')
        # this statement allows to get rid of the rows with incorrect dates
        df = df[df['date_of_birth'].notna()]

        # let's do the same for join_date
        df['join_date'] = pd.to_datetime(df['join_date'], infer_datetime_format=True, errors = 'coerce')
        # this statement allows to get rid of the rows with incorrect dates
        df = df[df['join_date'].notna()]

        # sort out some wrong country code entries for UK
        df.loc[(df['country'] == "United Kingdom") & (df['country_code'] != "GB"), 'country_code'] = 'GB'
        # remove some wrong entries
        df = df[df['country'].isin(['United Kingdom', 'Germany', 'United States'])]
        # returns the cleaned dataframe if required
        return df
    
    def clean_card_data(df):
        """
        Performs the cleaning of the card data.
        Removes any erroneous values, NULL values or errors with formatting.

            Parameters: a pandas dataframe

            Returns: a pandas dataframe

        """
        import pandas as pd
        import datetime
        df = df[df['card_number']!='NULL']
        df = df[df['card_provider'].isin(['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit',
       'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover',
       'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit'])]
        df['date_payment_confirmed'] = pd.to_datetime(df['date_payment_confirmed'], infer_datetime_format=True, errors = 'coerce')
        
        return df
    
    def clean_store_data(df):
        """
        Performs the cleaning of the stores data.
        Removes any erroneous values, NULL values or errors with formatting.

            Parameters: a pandas dataframe

            Returns: a pandas dataframe
        """
        df = df.drop(['index'], axis = 1)
        df = df[df.notna().any(axis=1)]
        df  = df[~df['lat'].notnull()]
        df.drop(columns = ['lat'], inplace = True)
        df['latitude'] = df['latitude'].astype(float).abs()

        import datetime
        import pandas as pd
        df['opening_date'] = pd.to_datetime(df['opening_date'], infer_datetime_format=True, errors = 'coerce')
        staff_mask = df['staff_numbers'].apply(pd.to_numeric, errors='coerce').isnull()
        
        import numpy as np
        mean_staff = df['staff_numbers'][staff_mask == False].astype(int).mean()
        df.loc[staff_mask == True, 'staff_numbers'] = mean_staff
        
        return df
    
    def clean_product_data(df):
        """
        Performs various cleaning actions on the product database

            Parameters:
                a dataframe containing product data from the product.csv file downloaded from the s3 datalake

            Returns:
                the same database clean from existing errors
        """
        import pandas as pd
        # remove rows with all null entries
        df = df[df['product_name'].notnull()]
        # create a column that contains the units of the weight column
        df['units'] = df['weight'].str.replace('\d+', '', regex=True).str.replace('.', '', regex=True)
        # analysis the 'units' column, create a list of values that make no sense
        list_of_values = ['GONZJTL', 'ZZTDGUZVU', 'MXRYSHX']
        # remove the rows which 'units' column contains any item in the list_of_values
        df = df[~df['units'].str.contains('|'.join(list_of_values))]
        # clean the price column from the £ sign
        df['product_price'] = df['product_price'].str.replace('£', '').astype(float)
         # clean the date column and transform it into a datetime object
        import datetime
        df['date_added'] = pd.to_datetime(df['date_added'], infer_datetime_format=True, errors = 'coerce')
        # sort the mispelled entries in the 'removed' column
        df['removed'] = df['removed'].str.replace('Still_avaliable', 'Still_available')

        return df
    
    def clean_product_weights(df):
        """
        Converts the weight column entries from various units to kg
        For those products with multiple items, calculates the total weight by multipling the 
        item weight x the number of itmes

           Parameters:
                a dataframe containing product data from the product.csv file downloaded from the s3 datalake

            Returns:
                the same database clean from existing errors

        """
        import pandas as pd
        # create an empty column that will contain the weight in kg
        import numpy as np
        df['weight_kg'] = np.nan

        # process the items such as "12 x 100g" by splitting those into a df with two colums, the index[0] containing the number of items
        # ("12") and the index[1] the weight of each item (100g). The weight is then cleaned from the unit.
        # the two are multiplied and then converted to kg
        df['weight_kg'] =  df[df['units'].str.contains('x')]['weight'].str.extract(r'(\d+)\s*x\s*(\d+)', expand=False)[0].astype(float) * df[df['units'].str.contains('x')]['weight'].str.extract(r'(\d+)\s*x\s*(\d+)', expand=False)[1].astype(float) * 0.001

        # this line just converts the columns with 'units' equal to kg into a float and assign it to the column 'weight clean"
        mask = df['units'] == 'kg'
        masked_df = df[mask]
        df.loc[mask, 'weight_kg'] = df.loc[mask, 'weight'].str.replace('kg', '').astype(float)

        # this line converts the columns with 'units' equal to g into a float, then converts to kg, and assign it to the column 'weight clean"
        mask = df['units'] == 'g'
        masked_df = df[mask]
        df.loc[mask, 'weight_kg'] = df.loc[mask, 'weight'].str.replace('g', '').astype(float) * 0.001

        # this line converts the columns with 'units' equal to ml into a float, then converts to kg, and assign it to the column 'weight clean"

        mask = df['units'] == 'ml'
        masked_df = df[mask]
        df.loc[mask, 'weight_kg'] = df.loc[mask, 'weight'].str.replace('ml', '').astype(float) * 0.001

        # this line converts the columns with 'units' equal to oz into a float, then converts to kg, and assign it to the column 'weight clean"
        mask = df['units'] == 'oz'
        masked_df = df[mask]
        df.loc[mask, 'weight_kg'] = df.loc[mask, 'weight'].str.replace('oz', '').astype(float) * 0.0283495

        # drop two columns made redundant by the cleaning process
        df = df.drop(['weight', 'units'], axis = 1)

        return df
