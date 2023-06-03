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
