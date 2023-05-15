class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and
    an S3 bucket.
    """

    def list_db_tables():
        """
        lists all the tables in the database
        """
        try:
            engine in globals()
        except NameError:
            print("SQLAlchemy engine not initialized.\n Please initialized it first")
        
