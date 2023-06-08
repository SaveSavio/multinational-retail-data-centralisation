# Multinational Retail Data Centralisation project

This repository contains the relevant code and information to complete the project. The project is assigned as part of the AiCore career development programme.

<u>Scenario</u>:<br>

You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

<u>Motivation</u>:<br>
In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location.

<u>Objectives</u>:<br>
1) The first goal will be to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.
2) The second goals is to then query the database to get up-to-date metrics for the business.

To complete the project, it is perform a set of tasks, that can be grouped into four Milestones:
1. Environment setup
1. Data Extraction and Cleaning
1. Database Creation
1. Exploratory data analysis

## Installation

Using pip package installer (https://pypi.org/project/pip/), run the following commands:

```python
pip install pandas
pip install numpy
pip install tabula-py
pip install requests
pip install boto3
pip install sqlalchemy
pip install psycopg2
pip install pyyaml
```
## Milestone 1: environment setup

It is necessary to create a postgreSQL database named **sales_data** with the following characteristics:

    DATABASE_TYPE = 'postgresql'
    HOST = 'localhost'
    USER = 'postgres'
    DATABASE = 'sales_data'
    PORT = 5432

## Milestone 2: Data Extraction

The data comes from a variety of sources:
- user data: AWS database in the cloud.
- card details: stored in a PDF document in an AWS S3 bucket
- The store data are stored as json files at several https urls and require the use of an API
- the product details are stored on a S3 server
- the orders are stored on a AWS RDS server

It needs to be extracted, cleaned and stored in preparation for its storage on a PostgreSQL database.


Three classes provide the methods needed to:
- Connect to source and download data
- Clean the data
- Upload the data to a Postgresql database on localhost named sales_data


```python
class DatabaseConnector:
    """
    Utility class. Defines the tools to connect, extract and upload data into the database.
    The methods contained will be fit to extract data from a particular data source.
    These sources include CSV files, an API and an S3 bucket.
    """

class DataCleaning:
    """
    Defines methods to clean data the user data from various datasources.
    """

class DataExtractor:
    """
    Defines methods that help extract data from different data sources such as
    CSV files, an API and an S3 bucket.
    """
```