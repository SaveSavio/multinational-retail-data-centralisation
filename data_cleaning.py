
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
        dataframe.drop(['Unnamed: 0', 'index', 'level_0', 'first_name', 'last_name', '1' ], axis = 1, inplace = True)
        return dataframe