# I should test if inspect is necessary
from sqlalchemy import create_engine 
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

## from ChatGPT

SELECT column_name::new_data_type
FROM table_name;

SELECT age::integer
FROM employees;

## from ChatGPT

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.expression import cast
from sqlalchemy.dialects.postgresql import ARRAY

# Create the SQLAlchemy engine
engine = create_engine('postgresql://username:password@localhost:5432/database')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a base class for declarative models
Base = declarative_base()


# Define a sample model
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# Perform a query with casting
session = Session()

# Cast the age column to the desired data type
query = session.query(Employee).add_columns(cast(Employee.age, String))

# Execute the query and fetch the results
results = query.all()

# Print the results
for employee, age in results:
    print(employee.name, age)

# Close the session
session.close()
