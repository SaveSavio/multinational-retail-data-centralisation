/* ###################### TASK # 1 ##################################################
The Operations team would like to know which countries we currently operate in and which country now has the most stores.
Perform a query on the database to get the information, it should return the following information:

+----------+-----------------+
| country  | total_no_stores |
+----------+-----------------+
| GB       |             265 |
| DE       |             141 |
| US       |              34 |
+----------+-----------------+
 */

SELECT 
       country_code, COUNT(country_code) AS total_no_stores
FROM 
    dim_store_details
GROUP BY 
    country_code
ORDER BY
    total_no_stores DESC;

/* ###################### TASK # 2 ##################################################
The business stakeholders would like to know which locations currently have the most stores.
They would like to close some stores before opening more in other locations.
Find out which locations have the most stores currently. The query should return the following:

+-------------------+-----------------+
|     locality      | total_no_stores |
+-------------------+-----------------+
| Chapletown        |              14 |
| Belper            |              13 |
| Bushley           |              12 |
| Exeter            |              11 |
| High Wycombe      |              10 |
| Arbroath          |              10 |
| Rutherglen        |              10 |
+-------------------+-----------------+
 */

SELECT 
       locality, COUNT(locality) AS total_no_stores
FROM 
    dim_store_details
GROUP BY 
    locality
ORDER BY
    total_no_stores DESC
LIMIT
    7;

/* ###################### TASK # 3 ##################################################
Query the database to find out which months typically have the most sales your query should return the following information:

+-------------+-------+
| total_sales | month |
+-------------+-------+
|   673295.68 |     8 |
|   668041.45 |     1 |
|   657335.84 |    10 |
|   650321.43 |     5 |
|   645741.70 |     7 |
|   645463.00 |     3 |
+-------------+-------+
 */

SELECT
	SUM (dim_products.product_price * orders_table.product_quantity) AS total_sales,
	EXTRACT (MONTH FROM dim_date_times.time_stamp) AS month
FROM
	orders_table
LEFT JOIN
	dim_products
ON
	orders_table.product_code = dim_products.product_code
LEFT JOIN
	dim_date_times
ON
	dim_date_times.date_uuid = orders_table.date_uuid
GROUP BY
	month
ORDER BY
    total_sales DESC
LIMIT
    6;

/* The company is looking to increase its online sales.
They want to know how many sales are happening online vs offline.
Calculate how many products were sold and the amount of sales made for online and offline purchases.
You should get the following information:

+------------------+-------------------------+----------+
| numbers_of_sales | product_quantity_count  | location |
+------------------+-------------------------+----------+
|            26957 |                  107739 | Web      |
|            93166 |                  374047 | Offline  |
+------------------+-------------------------+----------+
 */

WITH table_1 AS
    (
    SELECT *,
        CASE
            WHEN store_type = 'Web Portal' THEN 'Online'
            ELSE 'Offline'
        END AS on_off_line
    FROM
        dim_store_details
    )
SELECT
    COUNT(product_code) AS numbers_of_sales,
    SUM(product_quantity) AS product_quantity_count,
    on_off_line AS location
FROM
    orders_table
JOIN
    table_1
ON
    orders_table.store_code = table_1.store_code
GROUP BY
    on_off_line;

/* 
The sales team wants to know which of the different store types is generated the most revenue so they know where to focus.
Find out the total and percentage of sales coming from each of the different store types.
The query should return:

+-------------+-------------+---------------------+
| store_type  | total_sales | percentage_total(%) |
+-------------+-------------+---------------------+
| Local       |  3440896.52 |               44.87 |
| Web portal  |  1726547.05 |               22.44 |
| Super Store |  1224293.65 |               15.63 |
| Mall Kiosk  |   698791.61 |                8.96 |
| Outlet      |   631804.81 |                8.10 |
+-------------+-------------+---------------------+
 */

WITH table_1 AS
    (
    SELECT
        SUM(dim_products.product_price * orders_table.product_quantity) AS grand_total
    FROM
        orders_table
    LEFT JOIN
        dim_products
    ON
	    orders_table.product_code = dim_products.product_code
    ),
    table_2 AS
    (
    SELECT
        SUM(dim_products.product_price * orders_table.product_quantity) AS total_sales,
        store_type
    FROM
        orders_table
    LEFT JOIN
        dim_products
    ON
        orders_table.product_code = dim_products.product_code
    LEFT JOIN
        dim_store_details
    ON
        dim_store_details.store_code = orders_table.store_code
    GROUP BY
        store_type
    ORDER BY
        total_sales DESC
    )
    SELECT
        store_type,
        ROUND(CAST(total_sales AS numeric),2),
        ROUND(CAST(total_sales/grand_total * 100 AS NUMERIC),2) as "percentage_total(%)"
    FROM table_1, table_2;


/* The company stakeholders want assurances that the company has been doing well recently.
Find which months in which years have had the most sales historically.
The query should return the following information:

+-------------+------+-------+
| total_sales | year | month |
+-------------+------+-------+
|    27936.77 | 1994 |     3 |
|    27356.14 | 2019 |     1 |
|    27091.67 | 2009 |     8 |
|    26679.98 | 1997 |    11 |
|    26310.97 | 2018 |    12 |
|    26277.72 | 2019 |     8 |
|    26236.67 | 2017 |     9 |
|    25798.12 | 2010 |     5 |
|    25648.29 | 1996 |     8 |
|    25614.54 | 2000 |     1 |
+-------------+------+-------+
 */

    SELECT
        ROUND( CAST (SUM (dim_products.product_price * orders_table.product_quantity) AS NUMERIC), 2) AS total_sales,
        EXTRACT(YEAR FROM time_stamp) AS year,
        EXTRACT(MONTH FROM time_stamp) AS month
    FROM
        orders_table
    LEFT JOIN
        dim_products
    ON
	    orders_table.product_code = dim_products.product_code
    LEFT JOIN
        dim_date_times
    ON
        orders_table.date_uuid = dim_date_times.date_uuid
    GROUP BY
        year, month
    ORDER BY
        total_sales DESC
    LIMIT 10;

/* The operations team would like to know the overall staff numbers in each location around the world.
Perform a query to determine the staff numbers in each of the countries the company sells in.
The query should return the values:

+---------------------+--------------+
| total_staff_numbers | country_code |
+---------------------+--------------+
|               13307 | GB           |
|                6123 | DE           |
|                1384 | US           |
+---------------------+--------------+
 */

SELECT
    SUM(staff_numbers) as total_staff_numbers,
    country_code
FROM
    dim_store_details
GROUP BY
    country_code
ORDER BY
    total_staff_numbers DESC;


/* The sales team is looking to expand their territory in Germany.
Determine which type of store is generating the most sales in Germany.
The query will return:

+--------------+-------------+--------------+
| total_sales  | store_type  | country_code |
+--------------+-------------+--------------+
|   198373.57  | Outlet      | DE           |
|   247634.20  | Mall Kiosk  | DE           |
|   384625.03  | Super Store | DE           |
|  1109909.59  | Local       | DE           |
+--------------+-------------+--------------+

 */

SELECT
        ROUND( CAST (SUM (dim_products.product_price * orders_table.product_quantity) AS NUMERIC), 2) AS total_sales,
        dim_store_details.store_type,
        dim_store_details.country_code
    FROM
        orders_table
    LEFT JOIN
        dim_products
    ON
	    orders_table.product_code = dim_products.product_code
    LEFT JOIN
        dim_store_details
    ON
        orders_table.store_code = dim_store_details.store_code
    GROUP BY
        store_type, country_code
    HAVING
        country_code = 'DE'
    ORDER BY
        total_sales ASC;

/* Sales would like the get an accurate metric for how quickly the company is making sales.
Determine the average time taken between each sale grouped by year, the query should return the following information:

 +------+-------------------------------------------------------+
 | year |                           actual_time_taken           |
 +------+-------------------------------------------------------+
 | 2013 | "hours": 2, "minutes": 17, "seconds": 12, "millise... |
 | 1993 | "hours": 2, "minutes": 15, "seconds": 35, "millise... |
 | 2002 | "hours": 2, "minutes": 13, "seconds": 50, "millise... | 
 | 2022 | "hours": 2, "minutes": 13, "seconds": 6,  "millise... |
 | 2008 | "hours": 2, "minutes": 13, "seconds": 2,  "millise... |
 +------+-------------------------------------------------------+

Hint: You will need the SQL command LEAD. */

-- this is an explanation of the command, I won't need it all ---
-- SELECT time_stamp, LEAD(time_stamp) OVER (ORDER BY time_stamp) AS next_timestamp,
--        LEAD(time_stamp) OVER (ORDER BY time_stamp) - time_stamp AS elapsed_time
-- FROM dim_date_times;

SELECT
    year,
    AVG(elapsed_time) AS average_elapsed_time
FROM
    (
    SELECT 
        LEAD(time_stamp) OVER (ORDER BY time_stamp) - time_stamp AS elapsed_time,
        EXTRACT(YEAR FROM time_stamp) AS year
    FROM
        dim_date_times
    ) AS subquery
    GROUP BY
        YEAR
    ORDER BY
        average_elapsed_time DESC
    LIMIT 5;
