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
    ), table_2 AS
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