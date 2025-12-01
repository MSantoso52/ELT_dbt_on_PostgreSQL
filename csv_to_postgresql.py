import psycopg2
import csv
import io

def import_csv_to_postgresql(csv_filepath, table_name, db_params):
    """
    Imports data from a CSV file into a PostgreSQL table using the fast COPY FROM command.

    Args:
        csv_filepath (str): The path to the CSV file.
        table_name (str): The name of the target table in the database.
        db_params (dict): Dictionary containing database connection parameters.
    """
    conn = None
    try:
        # 1. Establish the connection
        conn = psycopg2.connect(**db_params)
        cursor = conn.cursor()

        print(f"Connection to PostgreSQL database successful.")

        # 2. Open the CSV file and read it into an in-memory buffer
        with open(csv_filepath, 'r') as f:
            # We use io.StringIO to treat the file content as a stream,
            # which is required by cursor.copy_from.
            # Skip the header row so COPY FROM only handles data rows.
            next(f) # Skips the first line (header) of the CSV
            
            # Use io.StringIO to buffer the rest of the file contents for copy_from
            csv_data = io.StringIO(f.read())
            
            # The CSV snippet had 5 columns: customer_id, full_name, address, city, zipcode
            columns = ['order_item_id', 'order_id', 'item_name', 'item_quantity', 'item_unit_price',  'item_total_price']
            column_names = ", ".join(columns)

            # 3. Use the COPY FROM command for efficient bulk loading
            cursor.copy_from(
                csv_data,          # The file-like object
                table_name,        # Target table name
                sep=',',           # CSV delimiter
                columns=columns    # List of column names in the table
            )

        # 4. Commit the transaction to save the changes
        conn.commit()
        print(f"Successfully imported data from '{csv_filepath}' to table '{table_name}'.")

    except (Exception, psycopg2.Error) as error:
        print(f"Error while connecting to PostgreSQL or during import: {error}")
        if conn:
            conn.rollback() # Rollback in case of error
    finally:
        # 5. Close the connection
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")

# --- Configuration ---

# 1. Database Connection Parameters (REPLACE WITH YOUR ACTUAL DETAILS)
DB_CONFIG = {
    "host": "127.0.0.1",
    "database": "customer_db",
    "user": "*****",
    "password": "*****",
    "port": "5432"
}

# 2. File and Table Details
CSV_FILE = "order_item_data.csv"
TARGET_TABLE = "orderitems" # Replace with your desired table name

# Run the import function
import_csv_to_postgresql(CSV_FILE, TARGET_TABLE, DB_CONFIG)

print("\nScript provided. Uncomment the last line and replace the configuration details to run the import.")
