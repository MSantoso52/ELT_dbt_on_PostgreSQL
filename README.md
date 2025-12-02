# Data Transformation on PostgreSQL with dbt
![Project Flow](postgres_dbt.png)
# *Project Overview* 
Demonstration of using the dbt (data build tool) framework to perform sophisticated data transformations directly within a PostgreSQL database environment.
The final output is a transformed dataset, like the customerrevenue table shown in the example, which is typically used for Business Intelligence (BI) and reporting.

# *Problem To Be Solved*
The project addresses the challenges associated with traditional data transformation (ELT) processes, which often suffer from:
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
   ❯ dbt debug
   16:28:37  Running with dbt=1.10.15
   16:28:37  dbt version: 1.10.15
   16:28:37  python version: 3.12.3
   16:28:37  python path: /home/mulyo/dbt_snowflake/bin/python3
   16:28:37  os info: Linux-6.8.0-88-generic-x86_64-with-glibc2.39
   16:28:37  Using profiles dir at /home/mulyo/.dbt
   16:28:37  Using profiles.yml file at /home/mulyo/.dbt/profiles.yml
   16:28:37  Using dbt_project.yml file at /home/mulyo/dbt_snowflake/psql_wh/dbt_project.yml
   16:28:37  adapter type: postgres
   16:28:37  adapter version: 1.9.1
   16:28:38  Configuration:
   16:28:38    profiles.yml file [OK found and valid]
   16:28:38    dbt_project.yml file [OK found and valid]
   16:28:38  Required dependencies:
   16:28:38   - git [OK found]

   16:28:38  Connection:
   16:28:38    host: localhost
   16:28:38    port: 5432
   16:28:38    user: postgres
   16:28:38    database: customer_db
   16:28:38    schema: customer
   16:28:38    connect_timeout: 10
   16:28:38    role: None
   16:28:38    search_path: None
   16:28:38    keepalives_idle: 0
   16:28:38    sslmode: None
   16:28:38    sslcert: None
   16:28:38    sslkey: None
   16:28:38    sslrootcert: None
   16:28:38    application_name: dbt
   16:28:38    retries: 1
   16:28:38  Registered adapter: postgres=1.9.1
   16:28:38    Connection test: [OK connection ok]

   16:28:38  All checks passed!
   ```
   ```bash
   ❯ dbt run
   16:32:11  Running with dbt=1.10.15
   16:32:11  Registered adapter: postgres=1.9.1
   16:32:11  [WARNING]: Configuration paths exist in your dbt_project.yml file which do not apply to any resources.
   There are 1 unused configuration paths:
   - models.psql_wh.example
   16:32:12  Found 1 model, 459 macros
   16:32:12
   16:32:12  Concurrency: 4 threads (target='dev')
   16:32:12
   16:32:12  1 of 1 START sql table model customer.customerrevenue .......................... [RUN]
   16:32:12  1 of 1 OK created sql table model customer.customerrevenue ..................... [SELECT 100 in 0.17s]
   16:32:12
   16:32:12  Finished running 1 table model in 0 hours 0 minutes and 0.33 seconds (0.33s).
   16:32:12
   16:32:12  Completed successfully
   16:32:12
   16:32:12  Done. PASS=1 WARN=0 ERROR=0 SKIP=0 NO-OP=0 TOTAL=1
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
