import oracledb

# Establish the database connection using TNS format
connection = oracledb.connect(
    user='hr',
    password='hr',
    dsn='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=orclpdb)))'
)
# Create a cursor object
cursor = connection.cursor()

# Function to insert data into a table
def insert_data(table_name, data):
    """
    Insert data into a table.

    Args:
    - table_name (str): The name of the table to insert data into.
    - data (dict): A dictionary where keys are column names and values are the data to insert.

    Example:
    insert_data('nutrition', {'name': 'Apple', 'calories': 52, 'protein': 0.3})
    """
    columns = ', '.join(data.keys())
    values = ', '.join([':' + key for key in data.keys()])
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    
    try:
        cursor.execute(sql, data)
        connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        connection.rollback()

# Function to delete data from a table
def delete_data(table_name, condition):
    """
    Delete data from a table.

    Args:
    - table_name (str): The name of the table to delete data from.
    - condition (str): The condition to specify which rows to delete.

    Example:
    delete_data('nutrition', "name='Apple'")
    """
    sql = f"DELETE FROM {table_name} WHERE {condition}"
    
    try:
        cursor.execute(sql)
        connection.commit()
        print("Data deleted successfully.")
    except Exception as e:
        print(f"Error deleting data: {e}")
        connection.rollback()

# Function to update data in a table
def update_data(table_name, data, condition):
    """
    Update data in a table.

    Args:
    - table_name (str): The name of the table to update data in.
    - data (dict): A dictionary where keys are column names and values are the new data to update.
    - condition (str): The condition to specify which rows to update.

    Example:
    update_data('nutrition', {'calories': 55}, "name='Apple'")
    """
    updates = ', '.join([f"{key}=:{key}" for key in data.keys()])
    sql = f"UPDATE {table_name} SET {updates} WHERE {condition}"
    
    try:
        cursor.execute(sql, data)
        connection.commit()
        print("Data updated successfully.")
    except Exception as e:
        print(f"Error updating data: {e}")
        connection.rollback()

# Function to query data from a table
def query_data(table_name, columns='*', condition=None):
    """
    Query data from a table.

    Args:
    - table_name (str): The name of the table to query data from.
    - columns (str or list): The columns to select. Default is '*'.
    - condition (str): The condition to specify which rows to query. Default is None.

    Example:
    query_data('nutrition', ['name', 'calories'], "calories > 50")
    """
    if isinstance(columns, list):
        columns = ', '.join(columns)
    
    sql = f"SELECT {columns} FROM {table_name}"
    if condition:
        sql += f" WHERE {condition}"
    
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print(f"Error querying data: {e}")

# Close the cursor and connection when done
cursor.close()
connection.close()
