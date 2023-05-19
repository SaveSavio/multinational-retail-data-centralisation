
class DataCleaning:
    """
    Defines methods to clean data from all datasources
    """
    def clean_user_data(df):
        
        """
        Performs the cleaning of the user data.
        You will need clean the user data, look out for NULL values, errors with dates, incorrectly
        typed values and rows filled with the wrong information.
        """
        import pandas as pd
        # drop the index columns, it is redundant
        df = df.drop(['index'], axis = 1)
        # sort out some wrong country code entries for UK
        df.loc[(df['country'] == "United Kingdom") & (df['country_code'] != "GB"), 'country_code'] = 'GB'
        # remove some wrong entries
        df = df[df['country'].isin(['United Kingdom', 'Germany', 'United States'])]
        # returns the cleaned dataframe if required
        return df