class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and
    an S3 bucket.
    """

    def list_db_tables(engine):
        """
        Lists all the tables names in the database

            Parameters:
                SQLalchemy engine object

            Returns:
                A list all the tables in the database
        """
        from sqlalchemy import inspect
        inspector = inspect(engine)
        table_names = inspector.get_table_names()
        return table_names
    
    
    def read_RDS_table(table_name, engine):
        """
        Extracts the database into a Pandas dataframe

            Parameters:
                table_name: a string containing the name of the table to be converted in a pandas dataframe
                engine: the SQLalchemy engine object 

            Returns:
                a Pandas dataframe containing the information of the input table
        """
        import pandas as pd
        df = pd.read_sql_table(table_name, engine)
        return df