# Data Transformation on PostgreSQL with dbt

# *Project Overview* 
This project to demonstrate data transformation using dbt.

# *Problem To Be Solved*
* The project addresses the challenges associated with traditional data transformation (ELT) processes, which often suffer from:
* Complexity and Maintenance: Transformation logic is typically scattered across unwieldy stored procedures, views, or custom scripts, making it hard to understand, debug, and update.
* Lack of Quality Control: Traditional SQL transformation lacks built-in mechanisms for testing, documentation, and data quality checks, leading to unreliable data products
* Poor Code Management: Transformations are often not version-controlled or modular, making collaboration difficult.
dbt solves this by enforcing software engineering best practices (like modularity, version control, and testing) on the data transformation layer, treating SQL as testable, deployable code.

# *Business Impact*
Implementing data transformation with dbt provides direct and measurable business benefits:
* Reliable Decision-Making: By enforcing data quality tests and documentation, dbt ensures the resulting data models (e.g., customer revenue metrics) are accurate and trustworthy, leading to better, evidence-based business decisions.
* Faster Time-to-Insight: Automated transformations and dependency management accelerate the process of turning raw data into valuable business metrics, allowing reporting and analytics to be updated quickly.
* Data Governance and Auditing: The project's structure automatically tracks data lineage—showing how raw data becomes a final metric. This is crucial for compliance and auditing.

# *Business Leverage*
The use of dbt creates significant organizational leverage by transforming the data workflow:
* Increased Data Team Agility: Data engineers and analysts become more productive by writing simple, modular SQL SELECT statements instead of complex DDL/DML scripts. They can iterate on transformation logic faster, responding quickly to new business requirements.
* Enabling Self-Service Analytics: The project results in clean, validated, and highly structured data marts (like the customerrevenue table). This stable foundation allows business users and data analysts to directly query these final tables for reporting and ad-hoc analysis, reducing their dependency on the data engineering team and enabling true self-service BI.
* Reduced Cloud/Database Costs: dbt promotes efficient, SQL-based transformations, allowing the database (PostgreSQL in this case) to perform the heavy lifting, which is often more scalable and cost-effective than running transformations outside the warehouse.

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
   host (hostname for the instance): localhost
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
# *Assumption*
1. PostgreSQL run on system (recomended on docker)
   ```bash
   psql -U postgres -h 127.0.0.1 -p 5432
   ```
3. Database created for CSV imported (exp: customer_db)
   ```sql
   customer_db=# \l
                                                       List of databases
       Name     |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |   Access privileges
   -------------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------
    customer_db | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
    postgres    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           |
   
   (2 rows)   
   ```
5. Table created (exp: cutomers, orders, orderitems)
   ```sql
   customer_db=# \d
           List of relations
    Schema |    Name    | Type  |  Owner
   --------+------------+-------+----------
    public | customers  | table | postgres
    public | orderitems | table | postgres
    public | orders     | table | postgres
   (3 rows)
   ```
