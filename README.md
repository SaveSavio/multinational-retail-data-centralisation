# Multinational Retail Data Centralisation
Scenario:<br>
You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team. In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location. Your first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data. You will then query the database to get up-to-date metrics for the business.

## Milestone 1: GitHub

- To create the GitHub repo that will store the code.

## Milestone 2: Data Extraction

The data comes from a variety of sources. It needs to be extracted, cleaned and stored in preparation for its storage on a PostgreSQL database.

- The SQL database is named **sales_data**. It's been created with PGAdmin and stored on a localhost.

- Three classes provide the methods needed to
    - Connect to source and download data
    - Clean the data
    - Upload the data to a Postgresql database on localhost named sales_data


```python
class DatabaseConnector:
    """
    Utility class.
    Defines the tools to connect, extract and upload data into the database.
    The methods contained will be fit to extract data from a particular data source.
    These sources include CSV files, an API and an S3 bucket.
    """
    
    def read_db_creds(creds_yaml):
        """
        Reads credentials from the yaml file and returns a dictionary of credentials
            
            Parameters: 
                yaml file containing the credential to connect to the database

            Returns:
                the credential in dictionary format
        """
        
    def init_db_engine(credentials):
        """
        Initializes and returns a SQLalchemy engine object

            Parameters:
                the credentials from the return of read_db_creds in form of a python dictionary
            
            Returns:    
                Initialises and returns an sqlalchemy database engine.
                
        """

    def upload_to_db(dataframe, table_name):
        """
         This method will take in a Pandas DataFrame and table name to upload to as an argument.
         It uploads the dataframe to the sales_data SQL database on the localhost.

            Parameters: a pandas dataframe to be uploaded, the 

            Returns: -

        """
        
```python
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
    
    def clean_card_data(df):
        """
        Performs the cleaning of the card data.
        Removes any erroneous values, NULL values or errors with formatting.

            Parameters: a pandas dataframe

            Returns: a pandas dataframe

        """

        return df
    
    def clean_store_data(df):
        """
        Performs the cleaning of the stores data.
        Removes any erroneous values, NULL values or errors with formatting.

            Parameters: a pandas dataframe

            Returns: a pandas dataframe
        """
    
    def clean_product_data(df):
        """
        Performs various cleaning actions on the product database

            Parameters:
                a dataframe containing product data from the product.csv file downloaded from the s3 datalake

            Returns:
                the same database clean from existing errors
        """
    
    def clean_product_weights(dfc):
        """
        Converts the weight column entries from various units to kg
        For those products with multiple items, calculates the total weight by multipling the 
        item weight x the number of itmes

           Parameters:
                a dataframe containing product data from the product.csv file downloaded from the s3 datalake

            Returns:
                the same database clean from existing errors

        """

    def clean_orders_data(df):
        """
        Cleans the orders_data downloaded from the AWS RDS server
            Parameters:
                A pandas dataframe

            Results:
                A pandas dataframe
        """

    def clean_date_details(df):
        """
        Cleans the sale date details

            Parameters: a pandas dataframe containing the sales information

            Returns: a pandas dataframe cleaned from erroneous values
        """
```
