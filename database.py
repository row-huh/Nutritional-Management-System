# CRUD OPERATIONS
# INSERT FUNCTIONS
# insert food
def insert_food_item(data, connection):
    try:
        # Create a cursor object from the existing connection
        cursor = connection.cursor()
        print(data)

        # auto_increment the food id
        get_ids = "SELECT food_item_id from Food_Item"
        cursor.execute(get_ids)
        ids = cursor.fetchall()
        print(ids)
        food_item_id = generate_unique_id(ids)

        # Prepare the SQL statement
        sql = f"INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES ({food_item_id}, :name, :calories, :protein, :carbs, :fats)"
        connection.commit()

        test_sql = "SELECT * FROM Food_Item"
        # Execute the SQL statement with the provided data
        cursor.execute(sql, data)
        cursor.execute(test_sql)
        output = cursor.fetchall()
        print(output)

        print("Food item inserted successfully.")

    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting food item: {error.message}")

    finally:
        # Close the cursor
        cursor.close()


# helper function
def generate_unique_id(ids):

    # Extract numbers from the list of tuples
    existing_ids = [item[0] for item in ids]
    possible_values = range(1, 1001)  # Assuming IDs range from 1 to 1000
    available_ids = [id for id in possible_values if id not in existing_ids]

    if available_ids:
        return min(available_ids)
    else:
        return None  # No available IDs left






## INSERT DATA

# insert fitness data, use helper function to generate unique id for the table
def insert_fitness_data(data, connection):
    #TODO
    ...
    
    
# insert meal plan
def insert_meal_plan(data, connection):
    #TODO
    ...

# insert nutritionist
def insert_nutritionist(data, connection):
    #TODO
    ...


# insert patient
def insert_patient(data, connection):
    #TODO
    ...





## FETCH ALL
# fetch all patients
def fetch_patients():
    #TODO
    ...

# fetch all food_item
def fetch_food_items():
    #TODO
    ...

# fetch all meal_plan
def fetch_meal_plan():
    #TODO
    ...

# fetch all nutritionist
def fetch_nutritionist():
    #TODO
    ...

# fetch all patient
def fetch_patient():
    #TODO
    ...


## DELETE FUNCTIONS


## UPDATE FUNCTIONS


## RUN SQL QUERY FUNCTION