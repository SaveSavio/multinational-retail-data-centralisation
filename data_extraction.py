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
    
    def retrieve_pdf_data(https_link):
        """
            Uses the tabula-py Python package to extract data from a pdf document

            Parameters:
                Takes in a link as an argument
            
            Returns:
                a pandas DataFrame containing the data in the pdf
        """
        import tabula
        import pandas as pd
        dfs = tabula.read_pdf(https_link, pages='all')
        # the pdf file has 1 header for each page so tabula returns 1 list per each page
        # it is therefore necessary to concatenate all the pages in one table
        df = pd.concat(dfs)
        return df
    
    def list_number_of_stores():
        import requests
        key = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}
        url = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        results = requests.get(url, headers = key)
        return results