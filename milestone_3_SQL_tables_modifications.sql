/* Change the data types to correspond to those seen in the table below.

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
    ALTER COLUMN date_uuid TYPE UUID,
    ALTER COLUMN date_uuid TYPE UUID,
    ALTER COLUMN card_number TYPE VARCHAR(19),
    ALTER COLUMN store_code TYPE VARCHAR(12),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN product_quantity TYPE SMALLINT;