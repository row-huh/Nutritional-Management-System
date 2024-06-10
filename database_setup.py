import oracledb

# Establish the database connection using TNS format

def connect():
    connection = oracledb.connect(
        user='hr',
        password='oracle',
        dsn='(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=localhost)(PORT=1521))(CONNECT_DATA=(SERVICE_NAME=freepdb1)))'
    )

    return connection


def initialize_database():
    connection = connect()
    cursor = connection.cursor()

    # SQL statements to drop tables if they exist
    drop_tables_sql = """
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE Fitness_Data CASCADE CONSTRAINTS';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
    /
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE Food_Item CASCADE CONSTRAINTS';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
    /
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE Meal_Plan CASCADE CONSTRAINTS';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
    /
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE Nutritionist CASCADE CONSTRAINTS';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
    /
    BEGIN
        EXECUTE IMMEDIATE 'DROP TABLE Patient CASCADE CONSTRAINTS';
    EXCEPTION
        WHEN OTHERS THEN
            IF SQLCODE != -942 THEN
                RAISE;
            END IF;
    END;
    /
    """

    # Execute the drop tables SQL
    for sql in drop_tables_sql.split('/'):
        if sql.strip():
            try:
                cursor.execute(sql)
            except oracledb.DatabaseError as e:
                print(f"Error executing SQL: {e}")
                print(f"Help: https://docs.oracle.com/error-help/db/{e.args[0].code}/")

    # SQL statements to create tables
    create_tables_sql = """
    -- Create Patient table
    CREATE TABLE Patient (
        patient_id NUMBER PRIMARY KEY,
        name VARCHAR2(100),
        age NUMBER,
        gender VARCHAR2(10),
        contact_info VARCHAR2(100)
    );

    -- Create Nutritionist table
    CREATE TABLE Nutritionist (
        nutritionist_id NUMBER PRIMARY KEY,
        name VARCHAR2(100),
        specialty VARCHAR2(100),
        contact_info VARCHAR2(100)
    );

    -- Create Meal_Plan table
    CREATE TABLE Meal_Plan (
        meal_plan_id NUMBER PRIMARY KEY,
        patient_id NUMBER,
        nutritionist_id NUMBER,
        start_date DATE,
        end_date DATE,
        description VARCHAR2(500),
        FOREIGN KEY (patient_id) REFERENCES Patient(patient_id),
        FOREIGN KEY (nutritionist_id) REFERENCES Nutritionist(nutritionist_id)
    );

    -- Create Food_Item table
    CREATE TABLE Food_Item (
        food_item_id NUMBER PRIMARY KEY,
        name VARCHAR2(100),
        calories NUMBER,
        protein NUMBER,
        carbs NUMBER,
        fats NUMBER
    );

    -- Create Fitness_Data table
    CREATE TABLE Fitness_Data (
        fitness_data_id NUMBER PRIMARY KEY,
        patient_id NUMBER,
        weight NUMBER,
        height NUMBER,
        bmi NUMBER,
        measurement_date DATE,
        FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
    );
    """

    # Execute the create tables SQL
    for sql in create_tables_sql.split(';'):
        if sql.strip():
            try:
                cursor.execute(sql)
            except oracledb.DatabaseError as e:
                print(f"Error executing SQL: {e}")
                print(f"Help: https://docs.oracle.com/error-help/db/{e.args[0].code}/")

    # SQL statements to insert data
    insert_data_sql = """
    -- Insert data into Patient table
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (1, 'John Doe', 25, 'Male', 'john.doe@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (2, 'Jane Smith', 30, 'Female', 'jane.smith@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (3, 'Alice Johnson', 22, 'Female', 'alice.johnson@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (4, 'Bob Brown', 28, 'Male', 'bob.brown@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (5, 'Carol White', 35, 'Female', 'carol.white@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (6, 'David Green', 40, 'Male', 'david.green@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (7, 'Eve Black', 45, 'Female', 'eve.black@example.com');
    INSERT INTO Patient (patient_id, name, age, gender, contact_info) VALUES (8, 'Frank Blue', 50, 'Male', 'frank.blue@example.com');

    -- Insert data into Nutritionist table
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (1, 'Dr. Smith', 'Sports Nutrition', 'sports.nutritionist@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (2, 'Dr. Johnson', 'Weight Management', 'weight.management@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (3, 'Dr. Allen', 'Pediatric Nutrition', 'pediatric.nutrition@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (4, 'Dr. Baker', 'Diabetes Nutrition', 'diabetes.nutrition@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (5, 'Dr. Clark', 'Renal Nutrition', 'renal.nutrition@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (6, 'Dr. Davis', 'Geriatric Nutrition', 'geriatric.nutrition@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (7, 'Dr. Evans', 'Oncology Nutrition', 'oncology.nutrition@example.com');
    INSERT INTO Nutritionist (nutritionist_id, name, specialty, contact_info) VALUES (8, 'Dr. Foster', 'Cardiac Nutrition', 'cardiac.nutrition@example.com');

    -- Insert data into Meal_Plan table
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (1, 1, 1, DATE '2024-06-01', DATE '2024-06-30', '30-day sports nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (2, 2, 2, DATE '2024-06-01', DATE '2024-06-30', '30-day weight management plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (3, 3, 3, DATE '2024-06-01', DATE '2024-06-30', '30-day pediatric nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (4, 4, 4, DATE '2024-06-01', DATE '2024-06-30', '30-day diabetes nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (5, 5, 5, DATE '2024-06-01', DATE '2024-06-30', '30-day renal nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (6, 6, 6, DATE '2024-06-01', DATE '2024-06-30', '30-day geriatric nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (7, 7, 7, DATE '2024-06-01', DATE '2024-06-30', '30-day oncology nutrition plan');
    INSERT INTO Meal_Plan (meal_plan_id, patient_id, nutritionist_id, start_date, end_date, description) VALUES (8, 8, 8, DATE '2024-06-01', DATE '2024-06-30', '30-day cardiac nutrition plan');

    -- Insert data into Food_Item table
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (1, 'Apple', 95, 0.5, 25, 0.3);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (2, 'Banana', 105, 1.3, 27, 0.4);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (3, 'Orange', 62, 1.2, 15, 0.2);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (4, 'Broccoli', 55, 3.7, 11, 0.6);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (5, 'Chicken Breast', 165, 31, 0, 3.6);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (6, 'Salmon', 233, 25, 0, 14);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (7, 'Egg', 78, 6, 1, 5);
    INSERT INTO Food_Item (food_item_id, name, calories, protein, carbs, fats) VALUES (8, 'Almonds', 576, 21, 22, 49);

    -- Insert data into Fitness_Data table
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (1, 1, 70, 175, 22.9, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (2, 2, 60, 160, 23.4, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (3, 3, 55, 165, 20.2, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (4, 4, 80, 180, 24.7, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (5, 5, 65, 170, 22.5, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (6, 6, 75, 175, 24.5, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (7, 7, 68, 160, 26.6, DATE '2024-06-01');
    INSERT INTO Fitness_Data (fitness_data_id, patient_id, weight, height, bmi, measurement_date) VALUES (8, 8, 90, 190, 24.9, DATE '2024-06-01');
    """

    # Execute the insert data SQL
    for sql in insert_data_sql.split(';'):
        if sql.strip():
            try:
                cursor.execute(sql)
            except oracledb.DatabaseError as e:
                print(f"Error executing SQL: {e}")
                print(f"Help: https://docs.oracle.com/error-help/db/{e.args[0].code}/")


    # Commit the transaction
    connection.commit()

    return connection
