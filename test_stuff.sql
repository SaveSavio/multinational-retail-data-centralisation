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
