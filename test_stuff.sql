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


