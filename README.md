# Data Transformation on PostgreSQL with dbt

# *Project Overview* 
This project to demonstrate data transformation using dbt.

# *Problem To Be Solved*

# *Business Impact*

# *Business Leverage*

# *Project Flow*
1. Install dbt on the system
   ```bash
   pip install dbt-core dbt-postgres
   ```
3. Configure dbt for postgresql
   ```bash
   dbt init
   ...
   Enter a number: 1
   host (hostname for the instance): locahost
   port [5432]:
   user (dev username): postgres
   pass (dev password):
   dbname (default database that dbt will build objects in): customer_db
   schema (default schema that dbt will build objects in): cutomer_data
   threads (1 or more) [1]: 4   
   ```
5. Import csv files into postgresql
   ```bash
   python3 csv_to_posgresql.py
   ```
7. Checking dbt & run dbt model
   ```bash
   dbt debug

   dbt run 
   ```
9. Checking the result
    ```sql
    customer_db=# \d customer.*
                        Table "customer.customerrevenue"
        Column    |          Type          | Collation | Nullable | Default
    --------------+------------------------+-----------+----------+---------
      ustomer_id  | integer                |           |          |
      ustomername | character varying(255) |           |          |
      ordercount  | bigint                 |           |          |
      revenue     | numeric                |           |          |

    customer_db=# select * from customer.customerrevenue limit 10;
     customer_id |   customername    | ordercount | revenue
    -------------+-------------------+------------+---------
           11031 | Alexander Palmer  |          3 |  583.19
           11011 | Chelsey Lopez     |          3 |  528.65
           11091 | Denise Ryan       |          4 |  835.24
           11041 | Kenneth Palmer    |          4 |  718.45
           11083 | Gabriel Lee       |          4 |  689.97
           11071 | Dylan Stone       |          5 | 1036.56
           11079 | Larry Thomas      |          5 |  968.86
           11040 | Andrew Tapia      |          5 |  943.89
           11043 | Teresa Moore      |          5 |  500.85
           11068 | Melissa Wilson MD |          5 |  493.47
    (10 rows)
    ```
# *Asumption*
1. PostgreSQL run on system (recomended on docker)
2. Database created for CSV imported (exp: customer_db)
3. Table created (exp: cutomers, orders, orderitems)
