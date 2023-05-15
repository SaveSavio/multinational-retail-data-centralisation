class DatabaseConnector:
    """
    Defines the tools to connect and upload data into the database
    Ref: Project Milestone2, Task2
    Attributes:
        ...
        ...
    """
    
    # def __init__(self)

    def read_db_creds(creds_yaml):
        """
        Reads credentials from the yaml file and returns a dictionary of credentials
        """
        
        import yaml

        with open(creds_yaml, 'r') as yaml_file:
            creds_dict = yaml.safe_load(yaml_file)
            # print(creds_dict)
            return(creds_dict)
        
    def init_db_engine(credentials):
        """
        Reads the credentials from the return of read_db_creds and initialises and returns an sqlalchemy database engine.
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
            print("SQL engine successfully initialized")
        except:
            print("Error initializing SQLalchemy engine")