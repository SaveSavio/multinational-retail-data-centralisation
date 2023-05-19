from sqlalchemy import create_engine, inspect
import pandas as pd
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'macchio'
DATABASE = 'sales_data'
PORT = 5432
# create SQLalchemy engine
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}") 
engine.connect()
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(table_names)


from sklearn.datasets import load_iris
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])

iris.to_sql('iris_dataset', engine, if_exists='replace')