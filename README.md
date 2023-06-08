# Multinational Retail Data Centralisation project

This repository contains the relevant code and necessary information to complete the project that is assigned as part of the AiCore career development programme.

<u>Scenario</u>:<br>

You work for a multinational company that sells various goods across the globe. Currently, their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

<u>Motivation</u>:<br>
In an effort to become more data-driven, your organisation would like to make its sales data accessible from one centralised location.

<u>Objectives</u>:<br>
1) The first goal is to produce a system that stores the current company data in a database so that it's accessed from one centralised location and acts as a single source of truth for sales data.
2) The second goals is to then query the database to get up-to-date metrics for the business.

The project consists in a set of tasks that can be grouped into four Milestones:
1. Environment setup
1. Data Extraction and Cleaning
1. Database Creation
1. Exploratory data analysis

## Installation

Ensure the following packates are installed or run the following commands using pip package installer (https://pypi.org/project/pip/):

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
- The stores data are stored as JSON files at several https urls and require the use of an API
- the product details are stored on a S3 server
- the orders are stored on a AWS RDS server

Data has to be extracted, cleaned and stored in preparation for its storage on a PostgreSQL database.


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

The sequence of actions that lead to the creation of the company central database is coded in the
main.py file called *milestone_2_main.py*.

Finally, the cleaned data tables are updloaded to the dabaset through the **upload_to_db** method.

The tables in the schema are:
- user data: AWS database in the cloud --> **dim_user_table**
- card details: stored in a PDF document in an AWS S3 bucket  --> **dim_card_details**
- The store data are stored as json files at several https urls and require the use of an API --> **dim_store_data**
- the product details are stored on a S3 server --> **dim_products**
- the orders are stored on a AWS RDS server --> **dim_order**

## Milestone 3: Create the Database Schema
It is necessary to create the correct connections, through a set of primary and secondary keys, thus creating a *schema*
that interconnects the data and allows powerful analyses.

A primary keys created in each of the tables prefixed with **dim**:

```SQL
ALTER TABLE dim_card_details 
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_date_times 
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_products 
ADD PRIMARY KEY (product_code);

ALTER TABLE dim_store_details 
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_users 
ADD PRIMARY KEY (user_uuid);
```
Corresponding foreign keys are created
in the orders_table to reference the primary keys.

This creates a star-based database schema. The commands are documented in
- milestone_3_SQL_tables_modifications.sql <br>

## Milestone 4: Data Analysis
It is now possible to perform any desired data analysis on the data. In this case, the is performed in postgreSQL.<br> These are the questions answered:
1. How many stores does the busness have and in which countries?
1. Which locations currently have the most stores?
1. Which months produce the average highest cost of sales typically?
1. How many sales are coming from online?
1. What percentage of sales come through each type of store?
1. Which month in each year produced the highest cost of sales?
1. What is the staff headcount?
1. Which German store is selling the most?
1.  How quickly is the company making sales?

