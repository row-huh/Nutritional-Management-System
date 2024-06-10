import oracledb

# Helper function to generate a unique ID
def generate_unique_id(ids):
    existing_ids = [item[0] for item in ids]
    possible_values = range(1, 1001)  # Assuming IDs range from 1 to 1000
    available_ids = [id for id in possible_values if id not in existing_ids]

    if available_ids:
        return min(available_ids)
    else:
        return None  # No available IDs left

# Insert food item
def insert_food_item(data, connection):
    try:
        cursor = connection.cursor()
        get_ids = "SELECT food_item_id FROM Food_Item"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        food_item_id = generate_unique_id(ids)

        sql = f"INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES ({food_item_id}, :name, :calories, :protein, :carbs, :fats)"
        cursor.execute(sql, data)
        connection.commit()
        print("Food item inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting food item: {error.message}")

    finally:
        cursor.close()

# Insert fitness data
def insert_fitness_data(data, connection):
    try:
        cursor = connection.cursor()
        get_ids = "SELECT fitness_data_id FROM Fitness_Data"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        fitness_data_id = generate_unique_id(ids)

        sql = f"INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES ({fitness_data_id}, :patient_id, :weight, :height, :bmi, :measurement_date)"
        cursor.execute(sql, data)
        connection.commit()
        print("Fitness data inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting fitness data: {error.message}")

    finally:
        cursor.close()

# Insert meal plan
def insert_meal_plan(data, connection):
    try:
        cursor = connection.cursor()
        get_ids = "SELECT meal_plan_id FROM Meal_Plan"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        meal_plan_id = generate_unique_id(ids)

        sql = f"INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES ({meal_plan_id}, :patient_id, :nutritionist_id, TO_DATE(:start_date, 'YYYY-MM-DD'), TO_DATE(:end_date, 'YYYY-MM-DD'), :description)"
        cursor.execute(sql, data)
        connection.commit()
        print("Meal plan inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting meal plan: {error.message}")

    finally:
        cursor.close()

# Insert nutritionist
def insert_nutritionist(data, connection):
    try:
        cursor = connection.cursor()
        get_ids = "SELECT nutritionist_id FROM Nutritionist"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        nutritionist_id = generate_unique_id(ids)

        sql = f"INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES ({nutritionist_id}, :name, :specialty, :contact_info)"
        cursor.execute(sql, data)
        connection.commit()
        print("Nutritionist inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting nutritionist: {error.message}")

    finally:
        cursor.close()

# Insert patient
def insert_patient(data, connection):
    try:
        cursor = connection.cursor()
        get_ids = "SELECT patient_id FROM Patient"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        patient_id = generate_unique_id(ids)

        sql = f"INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES ({patient_id}, :name, :age, :gender, :contact_info)"
        cursor.execute(sql, data)
        connection.commit()
        print("Patient inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting patient: {error.message}")

    finally:
        cursor.close()

# Fetch all records from a table
def fetch_all_records(table_name, connection):
    try:
        cursor = connection.cursor()
        sql = f"SELECT * FROM {table_name}"
        cursor.execute(sql)
        records = cursor.fetchall()
        return records

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error fetching records from {table_name}: {error.message}")
        return []

    finally:
        cursor.close()

# Fetch all patients
def fetch_patients(connection):
    return fetch_all_records("Patient", connection)

# Fetch all food items
def fetch_food_items(connection):
    return fetch_all_records("Food_Item", connection)

# Fetch all meal plans
def fetch_meal_plans(connection):
    return fetch_all_records("Meal_Plan", connection)

# Fetch all nutritionists
def fetch_nutritionists(connection):
    return fetch_all_records("Nutritionist", connection)

# Fetch all fitness data
def fetch_fitness_data(connection):
    return fetch_all_records("Fitness_Data", connection)


# Delete a record by ID
def delete_record(table_name, column_name, record_id, connection):
    cursor = connection.cursor()

    # if record which is to be deleted is patient
    if table_name.lower() == 'patient':
        try:

            # delete patient records from meal_plan table
            sql = f"DELETE FROM Meal_plan WHERE patient_id = :record_id"
            cursor.execute(sql, {"record_id": record_id})

            # delete patient records from fitness_data table
            sql = f"DELETE FROM fitness_data WHERE patient_id = :record_id"
            cursor.execute(sql, {"record_id": record_id})

            # delete from patients table
            sql = f"DELETE FROM {table_name} WHERE {column_name} = :record_id"
            cursor.execute(sql, {"record_id": record_id})

            connection.commit()
            print(f"Record with ID {record_id} deleted from {table_name}.")
            return "Sucess"
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error deleting record from {table_name}: {error.message}")
            return None

        finally:
            cursor.close()

    # if record to be deleted in nutritionist
    elif table_name.lower() == 'nutritionist':
        try:

            # delete nutritionist records from meal_plan table
            sql = f"DELETE FROM Meal_plan WHERE nutritionist_id = :record_id"
            cursor.execute(sql, {"record_id": record_id})

            cursor = connection.cursor()
            # delete from nutritionist table
            sql = f"DELETE FROM {table_name} WHERE {column_name} = :record_id"
            cursor.execute(sql, {"record_id": record_id})

            connection.commit()
            print(f"Record with ID {record_id} deleted from {table_name}.")
            return "Success"

        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error deleting record from {table_name}: {error.message}")
            return None

        finally:
            cursor.close()
    else:
        try:
            cursor = connection.cursor()
            sql = f"DELETE FROM {table_name} WHERE {column_name} = :record_id"
            cursor.execute(sql, {"record_id": record_id})
            connection.commit()
            print(f"Record with ID {record_id} deleted from {table_name}.")
            return "Sucess"
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error deleting record from {table_name}: {error.message}")
            return None

        finally:
            cursor.close()


# Update a record by ID
def update_record(table_name, columns, record_id, update_data, connection):

    try:
        cursor = connection.cursor()
        update_fields = ', '.join([f"{col} = :{col}" for col in update_data.keys()])
        sql = f"UPDATE {table_name} SET {update_fields} WHERE {columns[0]} = :table_id"  # Assuming the first column is the primary key
        update_data["table_id"] = record_id
        cursor.execute(sql, update_data)
        connection.commit()
        print(f"Record with ID {record_id} updated in {table_name}.")
        return (f"Record with ID {record_id} updated in {table_name}.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error updating record in {table_name}: {error.message}")
        return None


    finally:
        cursor.close()


# Run a custom SQL query
def run_sql_query(query, connection):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error executing query: {error.message}")
        return []

    finally:
        cursor.close()
