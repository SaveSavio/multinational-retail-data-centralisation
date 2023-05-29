/* ################ TASK 1 ##################
Change the data types to correspond to those seen in the table below.

+------------------+--------------------+--------------------+
|   orders_table   | current data type  | required data type |
+------------------+--------------------+--------------------+
| date_uuid        | TEXT               | UUID               |
| user_uuid        | TEXT               | UUID               |
| card_number      | TEXT               | VARCHAR(?)         |
| store_code       | TEXT               | VARCHAR(?)         |
| product_code     | TEXT               | VARCHAR(?)         |
| product_quantity | BIGINT             | SMALLINT           |
+------------------+--------------------+--------------------+
 */


-- card number was cast as a bigint
-- it does not really matter, I will convert it to text here

-- SELECT
--     max(length(card_number)) as card_number_len,
--     max(length(store_code)) as store_code_len,
--     max(length(product_code)) as product_code_len
-- FROM orders_table;

-- ALTER TABLE IF EXISTS orders_table
--     ALTER COLUMN date_uuid TYPE UUID,
--     ALTER COLUMN date_uuid TYPE UUID,
--     ALTER COLUMN card_number TYPE VARCHAR(19),
--     ALTER COLUMN store_code TYPE VARCHAR(12),
--     ALTER COLUMN product_code TYPE VARCHAR(11),
--     ALTER COLUMN product_quantity TYPE SMALLINT;




/* ################ TASK 2 ##################
The column required to be changed in the users table are as follows:

+----------------+--------------------+--------------------+
| dim_user_table | current data type  | required data type |
+----------------+--------------------+--------------------+
| first_name     | TEXT               | VARCHAR(255)       |
| last_name      | TEXT               | VARCHAR(255)       |
| date_of_birth  | TEXT               | DATE               |
| country_code   | TEXT               | VARCHAR(?)         |
| user_uuid      | TEXT               | UUID               |
| join_date      | TEXT               | DATE               |
+----------------+--------------------+--------------------+
 */


-- SELECT
--     max(length(country_code)) as country_code_len
-- FROM dim_users;

-- ALTER TABLE IF EXISTS dim_users
--     ALTER COLUMN first_name TYPE VARCHAR(255),
--     ALTER COLUMN last_name TYPE VARCHAR(255),
--     ALTER COLUMN date_of_birth TYPE DATE,
--     ALTER COLUMN country_code TYPE VARCHAR(2),
--     ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
--     ALTER COLUMN join_date TYPE DATE;

/* ################ TASK 3 ##################
There are two latitude columns in the store details table.
Using SQL, merge one of the columns into the other so you have one latitude column.
    This task in not performed as I sorted the latitude column in the data cleaning process
Then set the data types for each column as shown below:

+---------------------+-------------------+------------------------+
| store_details_table | current data type |   required data type   |
+---------------------+-------------------+------------------------+
| longitude           | TEXT              | FLOAT                  |
| locality            | TEXT              | VARCHAR(255)           |
| store_code          | TEXT              | VARCHAR(?)             |
| staff_numbers       | TEXT              | SMALLINT               |
| opening_date        | TEXT              | DATE                   |
| store_type          | TEXT              | VARCHAR(255) NULLABLE  |
| latitude            | TEXT              | FLOAT                  |
| country_code        | TEXT              | VARCHAR(?)             |
| continent           | TEXT              | VARCHAR(255)           |
+---------------------+-------------------+------------------------+ */

-- SELECT
--     max(length(store_code)) as store_code_len
-- FROM dim_store_details;

SELECT *
FROM dim_store_details
WHERE store_code LIKE '%1388012W'

-- ALTER TABLE IF EXISTS dim_store_details
--     ALTER COLUMN longitude TYPE FLOAT,
--     ALTER COLUMN locality TYPE VARCHAR(255),
--     ALTER COLUMN store_code TYPE VARCHAR(11),
--     ALTER COLUMN staff_numbers TYPE SMALLING,
--     ALTER COLUMN opening_date TYPE DATE,
--     ALTER COLUMN store_type TYPE VARCHAR(255) NULLABLE
--     ALTER COLUMN latitude TYPE FLOAT,
--     ALTER COLUMN country_code TYPE VARCHAR(?),
--     ALTER COLUMN continent TYPE VARCHAR(255);