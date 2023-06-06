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
        ROUND(CAST SUM(dim_products.product_price * orders_table.product_quantity AS NUMERIC) AS total_sales,
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



-- SELECT EXTRACT(MONTH FROM date_column) AS month,
--        EXTRACT(YEAR FROM date_column) AS year,
--        SUM(sales_amount) AS total_sales
-- FROM your_table
-- GROUP BY EXTRACT(MONTH FROM date_column), EXTRACT(YEAR FROM date_column)
-- ORDER BY year, month;