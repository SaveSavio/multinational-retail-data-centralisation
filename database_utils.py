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
        
        import yaml

        with open(creds_yaml, 'r') as yaml_file:
            creds_dict = yaml.safe_load(yaml_file)
            # print(creds_dict)
            return(creds_dict)
        
    def init_db_engine(credentials):
        """
        Initializes and returns a SQLalchemy engine object

            Parameters:
                the credentials from the return of read_db_creds in form of a python dictionary
            
            Returns:    
                Initialises and returns an sqlalchemy database engine.
        """

        from sqlalchemy import create_engine

        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = credentials['RDS_HOST']
        USER = credentials['RDS_USER']
        PASSWORD = credentials['RDS_PASSWORD']
        DATABASE = credentials['RDS_DATABASE']
        PORT = credentials['RDS_PORT']
        # create SQLalchemy engine
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
        # checks connectivity
        try:
            engine.connect()
            print("SQL engine successfully connected")
            return engine
        except:
            print("Error initializing SQLalchemy engine")
        
    def upload_to_db(dataframe, table_name):
        """
         This method will take in a Pandas DataFrame and table name to upload to as an argument.
        """
        # I should test if inspect is necessary
        from sqlalchemy import create_engine, inspect
        import pandas as pd
        # the engine is implemented statically to the sales_data database
        # but we have the tools to make this more "dynamic" by passing the engine parameter
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        HOST = 'localhost'
        USER = 'postgres'
        PASSWORD = 'macchio'
        DATABASE = 'sales_data'
        PORT = 5432
        # create SQLalchemy engine for the sales_data database
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
        # connect the engine
        engine.connect()
        # upload the database to the SQL database with the pandas method .to_sql
        dataframe.to_sql(table_name, engine, if_exists='replace')