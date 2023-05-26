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
    
    def list_number_of_stores(url, key):
        
        """
        Retrieves the number of stores from the endpoint

            Parameters:
                url: endpoint url
                key: dictionary key to connect to the API in the method's header

            Returns:
                the number of stores to be extracted later
        """
        import requests
        results = requests.get(url, headers = key)
        return results.json()['number_stores']
    
    def retrieve_stores_data(base_url, number_stores, key):
        """
        Retrieve a store endpoint as an argument and extracts all the stores from the API saving them in a pandas DataFrame.
            Parameters:
                base_url: stores endpoint
                the number of stores (an integer) that have to be extracted
                an authentication key to be passed in the requests.get header
            Returns:
                A pandas dataframe containing all stores information
        """
       
        import pandas as pd
        import requests
        
        df = pd.DataFrame()

        for index in range(number_stores):
            url = base_url + str(index)
            store = requests.get(url, headers = key)
            tmp = pd.json_normalize(store.json())
            df = pd.concat([df, tmp], ignore_index=True)
            print(index+1, end="")
        return df
    
    def extract_from_s3(s3_url):
        """
        Uses a boto3 package to download data from a S3 server
        You must log into AWS CLI before running this method
        the method requires a s3 bucket url as parameter
        anyway it does not provide flexibility to chose the key and filename
        
            Parameters:
                s3_datalake_address

            Returns: 
                a pandas dataframe

        """
        # extract the datalake Bucket from the address line
        import re
        start = 's3://'
        end = '/'
        bucket = re.search('%s(.*)%s' % (start, end), s3_url).group(1)
        filename = 'product.csv'
        # use boto3 client to manage the communication with the s3
        import boto3
        s3_client = boto3.resource('s3')
        s3_client.Bucket(bucket).download_file(Key='products.csv', Filename=filename)

        import pandas as pd
        return pd.read_csv(filename)