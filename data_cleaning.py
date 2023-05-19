
class DataCleaning:
    """
    Defines methods to clean data from all datasources
    """
    def clean_user_data(dataframe):
        
        """
        Performs the cleaning of the user data.
        You will need clean the user data, look out for NULL values, errors with dates, incorrectly
        typed values and rows filled with the wrong information.
        """
        import pandas as pd
        #dataframe.drop(['index', 'level_0', 'first_name', 'last_name', '1' ], axis = 1, inplace = True)
        dataframe = dataframe.drop(['index'], axis = 1)
        dataframe.loc[(dataframe['country'] == "United Kingdom") & (dataframe['country_code'] != "GB"), 'country_code'] = 'GB'
        dataframe = dataframe[~dataframe['country'].isin(['I7G4DMDZOZ', 'AJ1ENKS3QL', 'XGI7FM0VBJ', 'S0E37H52ON', 'XN9NGL5C0B',
       '50KUU3PQUF', 'EWE3U0DZIV', 'GMRBOMI0O1', 'YOTSVPRBQ7', '5EFAFD0JLI', 'PNRMPSYR1J', 'RQRB7RMTAD', '3518UD5CE8',
       '7ZNO5EBALT', 'T4WBZSW0XI'])]
        return dataframe