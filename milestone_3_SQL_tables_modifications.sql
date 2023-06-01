
/* ############################ TASK 1 #########################################
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

SELECT
    max(length(card_number)) as card_number_len,
    max(length(store_code)) as store_code_len,
    max(length(product_code)) as product_code_len
FROM orders_table;


ALTER TABLE IF EXISTS orders_table
    ALTER COLUMN date_uuid TYPE UUID USING date_uuid::uuid,
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_quantity TYPE SMALLINT USING product_quantity::smallint;



/* ########################### TASK 2 ###############################################
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

ALTER TABLE IF EXISTS dim_users
    ALTER COLUMN first_name TYPE VARCHAR(255),
    ALTER COLUMN last_name TYPE VARCHAR(255),
    ALTER COLUMN date_of_birth TYPE DATE,
    ALTER COLUMN country_code TYPE VARCHAR(2),
    ALTER COLUMN user_uuid TYPE UUID USING user_uuid::uuid,
    ALTER COLUMN join_date TYPE DATE;

/* ######################### TASK 3 ###################################################
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


UPDATE dim_store_details
SET longitude = NULL 
WHERE store_type = 'Web Portal';


UPDATE dim_store_details
SET staff_numbers = '50' 
WHERE staff_numbers LIKE '46.9%';

-- SELECT *
-- FROM dim_store_details
-- WHERE store_type = 'Web Portal';

ALTER TABLE IF EXISTS dim_store_details
    ALTER COLUMN longitude TYPE FLOAT USING longitude::float,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(12),
--    ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT,
    ALTER COLUMN opening_date TYPE DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255), -- not sure how to cast nullable
    ALTER COLUMN latitude TYPE FLOAT USING latitude::float,
    ALTER COLUMN country_code TYPE VARCHAR(12),
    ALTER COLUMN continent TYPE VARCHAR(255);

/* ######################## TASK 4 ##########################################################
You will need to do some work on the products table before casting the data types correctly.
The product_price column has a £ character which you need to remove using SQL. --> I already did this in pandas
The team that handles the deliveries would like a new human-readable column added for the weight
so they can quickly make decisions on delivery weights.
Add a new column weight_class which will contain human-readable values based on the weight range of the product.

+--------------------------+-------------------+
| weight_class VARCHAR(?)  | weight range(kg)  |
+--------------------------+-------------------+
| Light                    | < 2               |
| Mid_Sized                | >= 2 - < 40       |
| Heavy                    | >= 40 - < 140     |
| Truck_Required           | => 140            |
+----------------------------+-----------------+
 */

ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(255);

UPDATE dim_products
SET weight_class = 
  CASE
    WHEN weight_kg < 2 THEN 'Light'
    WHEN weight_kg BETWEEN 2 AND 40 THEN 'Mid_Sized'
    WHEN weight_kg BETWEEN 40 AND 140 THEN 'Heavy'
    ELSE 'Truck_Required'
  END;

-- SELECT


/* ######################### TASK 5 #################################################
After all the columns are created and cleaned, change the data types of the products table.
You will want to rename the removed column to still_available before changing its data type.
Make the changes to the columns to cast them to the following data types:

+-----------------+--------------------+--------------------+
|  dim_products   | current data type  | required data type |
+-----------------+--------------------+--------------------+
| product_price   | TEXT               | FLOAT              |
| weight          | TEXT               | FLOAT              |
| EAN             | TEXT               | VARCHAR(?)         |
| product_code    | TEXT               | VARCHAR(?)         |
| date_added      | TEXT               | DATE               |
| uuid            | TEXT               | UUID               |
| still_available | TEXT               | BOOL               |
| weight_class    | TEXT               | VARCHAR(?)         |
+-----------------+--------------------+--------------------+
 */

-- SELECT
--     max(length("EAN")) as EAN_len,
--     max(length(product_code)) as product_code_len,
--     max(length(weight_class)) as weight_class_len
-- FROM dim_products;

ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

-- I have to change the removed table to a boolean by
-- substituting the categories with a BOOL

ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOLEAN
USING (still_available = 'Still_available');


ALTER TABLE IF EXISTS dim_products
    ALTER COLUMN product_price TYPE FLOAT USING product_price::float,
    ALTER COLUMN weight_kg TYPE  FLOAT USING weight_kg::float,
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN date_added TYPE DATE,
    ALTER COLUMN uuid TYPE UUID  USING uuid::UUID,
    ALTER COLUMN still_available TYPE BOOL,
    ALTER COLUMN weight_class TYPE VARCHAR(14);


/* ###################### TASK 6 ###########################################
Now update the date table with the correct types:

+-----------------+-------------------+--------------------+
| dim_date_times  | current data type | required data type |
+-----------------+-------------------+--------------------+
| month           | TEXT              | VARCHAR(?)         |
| year            | TEXT              | VARCHAR(?)         |
| day             | TEXT              | VARCHAR(?)         |
| time_period     | TEXT              | VARCHAR(?)         |
| date_uuid       | TEXT              | UUID               |
+-----------------+-------------------+--------------------+
 */

-- SELECT
-- --    max(length(month)) as month_len, -- I have deleted the month, year, day columns basically because it is redundant
-- --    max(length(year)) as year_len,
-- --    max(length(day)) as day_len,
--     max(length(time_period)) as time_period_len
-- FROM dim_date_times;

ALTER TABLE IF EXISTS dim_date_times
     ALTER COLUMN time_period TYPE VARCHAR(10),
     ALTER COLUMN date_uuid TYPE UUID  USING date_uuid::UUID;


/* ###################### TASK 7 ##############################################
Now we need to update the last table for the card details.
Make the associated changes after finding out what the lengths of each variable should be:

+------------------------+-------------------+--------------------+
|    dim_card_details    | current data type | required data type |
+------------------------+-------------------+--------------------+
| card_number            | TEXT              | VARCHAR(?)         |
| expiry_date            | TEXT              | VARCHAR(?)         |
| date_payment_confirmed | TEXT              | DATE               |
+------------------------+-------------------+--------------------+
 */

SELECT
    max(length(card_number)) as card_num_len,
    max(length(expiry_date)) as expiry_date_len
FROM dim_card_details;

ALTER TABLE IF EXISTS dim_card_details
    ALTER COLUMN card_number TYPE VARCHAR(19),
     ALTER COLUMN expiry_date TYPE VARCHAR(5),
     ALTER COLUMN date_payment_confirmed TYPE DATE;


/* #################### TASK 8 ############################################
Now that the tables have the appropriate data types we can begin adding the primary keys to each of the tables prefixed with dim.
Each table will serve the orders_table which will be the single source of truth for our orders.
Check the column header of the orders_table you will see all but one of the columns exist in one of our tables prefixed with dim.
We need to update the columns in the dim tables with a primary key that matches the same column in the orders_table.
Using SQL, update the respective columns as primary key columns. */

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

SELECT product_code
FROM dim_products
WHERE product_code IS NULL;

/* 
With the primary keys created in the tables prefixed with dim we can now create the foreign keys in the orders_table
to reference the primary keys in the other tables.
Use SQL to create those foreign key constraints that reference the primary keys of the other table.
This makes the star-based database schema complete.
*/

/* 
    referencing_table is the name of the table that will contain the foreign key ----> orders_table
    fk_constraint_name is an optional name you can give to the foreign key constraint.
    referencing_column is the column in the referencing_table that will hold the foreign key values ---> orders_table.column
    referenced_table is the name of the table being referenced.
    referenced_column is the column in the referenced_table that is being referenced.
 */
ALTER TABLE orders_table
ADD CONSTRAINT fk_card_number
FOREIGN KEY (card_number)
REFERENCES dim_card_details (card_number);

ALTER TABLE orders_table
ADD CONSTRAINT fk_date_uuid
FOREIGN KEY (date_uuid)
REFERENCES dim_date_times (date_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT fk_product_code
FOREIGN KEY (product_code)
REFERENCES dim_products (product_code);

ALTER TABLE orders_table
ADD CONSTRAINT fk_store_code
FOREIGN KEY (store_code)
REFERENCES dim_store_details (store_code);

ALTER TABLE orders_table
ADD CONSTRAINT fk_user_uuid
FOREIGN KEY (user_uuid)
REFERENCES dim_users (user_uuid);


