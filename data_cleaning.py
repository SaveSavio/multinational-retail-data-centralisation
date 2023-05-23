
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