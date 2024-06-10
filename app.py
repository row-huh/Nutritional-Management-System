from flask import Flask, render_template, request
import database as db
import database_setup as dbsetup
import helper as h

app = Flask(__name__)
connection = dbsetup.initialize_database()


landing_page = 'dashboard.html'
new = 'update.html'



# landing page
@app.route('/')
def index():
    all_patients, all_nutritionists, all_fitness_data, all_food_items, all_meal_plans = h.html_data(connection)
    return render_template(landing_page, message=None, all_patients=all_patients, all_nutritionists=all_nutritionists, all_fitness_data=all_fitness_data, all_food_items=all_food_items, all_meal_plans=all_meal_plans)


# insert food item
@app.route('/submit_food_item', methods=['POST'])
def submit_food():
    form_data = request.form.to_dict()
    db.insert_food_item(form_data, connection)
    message= "New food item created successfully"

    return render_template(landing_page, message=message)

# insert patient
@app.route('/submit_patient', methods=['POST'])
def submit_patient():
    form_data = request.form.to_dict()
    db.insert_patient(form_data, connection)
    message= "New Patient created successfully"
    return render_template(landing_page, message=message)


# insert nutritionist
@app.route('/submit_nutritionist', methods=['POST'])
def submit_nutritionist():
    form_data = request.form.to_dict()
    db.insert_nutritionist(form_data, connection)
    message= "New Nutritionist created successfully"
    return render_template(landing_page, message=message)


# insert meal_plan
@app.route('/submit_meal_plan', methods=['POST'])
def submit_meal_plan():
    form_data = request.form.to_dict()
    print(form_data)
    db.insert_meal_plan(form_data, connection)
    message= "New meal plan created successfully"
    return render_template(landing_page, message=message)


# insert fitness_data
@app.route('/submit_fitness_data', methods=['POST'])
def submit_fitness_data():
    form_data = request.form.to_dict()
    db.insert_fitness_data(form_data, connection)
    message= "New fitness data created successfully"
    return render_template(landing_page, message=message)



# delete food_item
@app.route('/delete_food_item', methods=['POST'])
def delete_food_item():
    id = request.form.get('food_item_id')
    print(id)
    
    if db.delete_record('food_item', 'food_item_id', id, connection):
        message= f"Food item with id {id} deleted successfully"
        return render_template(landing_page, message=message, err_message=None)
    else:
        err_message= f"Something went wrong with deleting"
        return render_template(landing_page, err_message=err_message, message=None)


# delete nutritionist
@app.route('/delete_nutritionist', methods=['POST'])
def delete_nutritionist():
    id = request.form.get('nutritionist_id')
    print(id)
    
    if db.delete_record('nutritionist', 'nutritionist_id', id, connection):
        message= f"Nutritionist with id {id} deleted successfully"
        return render_template(landing_page, message=message, err_message=None)
    else:
        err_message= f"Something went wrong with deleting"
        return render_template(landing_page, err_message=err_message, message=None)


# delete patient
@app.route('/delete_patient', methods=['POST'])
def delete_patient():
    id = request.form.get('patient_id')
    print(id)
    
    if db.delete_record('patient', 'patient_id', id, connection):
        message= f"Patient with id {id} deleted successfully"
        return render_template(landing_page, message=message, err_message=None)
    else:
        err_message= f"Something went wrong with deleting"
        return render_template(landing_page, err_message=err_message, message=None)


# delete meal_plan
@app.route('/delete_meal_plan', methods=['POST'])
def delete_meal_plan():
    id = request.form.get('meal_plan_id')
    print(id)
    
    if db.delete_record('meal_plan', 'meal_plan_id', id, connection):
        message= f"Meal plan with id {id} deleted successfully"
        return render_template(landing_page, message=message, err_message=None)
    else:
        err_message= f"Something went wrong with deleting"
        return render_template(landing_page, err_message=err_message, message=None)


# delete fitness_data
@app.route('/delete_fitness_data', methods=['POST'])
def delete_fitness_data():
    id = request.form.get('fitness_data_id')
    print(id)
    
    if db.delete_record('fitness_data', 'fitness_data_id', id, connection):
        message= f"Fitness data with id {id} deleted successfully"
        return render_template(landing_page, message=message, err_message=None)
    else:
        err_message= f"Something went wrong with deleting"
        return render_template(landing_page, err_message=err_message, message=None)



# load update.html
@app.route('/fetch_food_item_details', methods=["POST"])
def fetch_food_item_details():
    food_item_id = request.form.get('food_item_id')
    print(food_item_id)
    query = f"SELECT * FROM Food_item WHERE food_item_id={food_item_id}"
    data = db.run_sql_query(query , connection)
    print(data)
    html_form = h.get_update_html('food_item', data)
    return render_template(new, html_form=html_form)

# fetch update nutritionist form
@app.route('/fetch_nutritionist_details', methods=["POST"])
def fetch_nutritionist_details():
    nutritionist_id = request.form.get('nutritionist_id')
    query = f"SELECT * FROM Nutritionist WHERE nutritionist_id={nutritionist_id}"
    data = db.run_sql_query(query, connection)
    html_form = h.get_update_html('nutritionist', data)
    return render_template('update.html', html_form=html_form)


# fetch update meal plan form 
@app.route('/fetch_meal_plan_details', methods=["POST"])
def fetch_meal_plan_details():
    meal_plan_id = request.form.get('meal_plan_id')
    query = f"SELECT * FROM Meal_Plan WHERE meal_plan_id={meal_plan_id}"
    data = db.run_sql_query(query, connection)
    html_form = h.get_update_html('meal_plan', data)
    return render_template('update.html', html_form=html_form)


# fetch update fitness data form
@app.route('/fetch_fitness_data_details', methods=["POST"])
def fetch_fitness_data_details():
    fitness_data_id = request.form.get('fitness_data_id')
    query = f"SELECT * FROM Fitness_Data WHERE fitness_data_id={fitness_data_id}"
    data = db.run_sql_query(query, connection)
    html_form = h.get_update_html('fitness_data', data)
    return render_template('update.html', html_form=html_form)


# fetch update patient form
@app.route('/fetch_patient_details', methods=["POST"])
def fetch_patient_details():
    patient_id = request.form.get('patient_id')
    query = f"SELECT * FROM Patient WHERE patient_id={patient_id}"
    data = db.run_sql_query(query, connection)
    html_form = h.get_update_html('patient', data)
    return render_template('update.html', html_form=html_form)



# update details
# update food item
@app.route('/update_food_item', methods=["POST"])
def update_food_item():
    updates = request.form.to_dict()
    print("Updates", updates)
    record_id = updates['food_item_id']
    print("Record id", record_id)
    result = db.update_record('food_item', h.food_item_columns, record_id=record_id, update_data=updates, connection=connection)
    print("RESULT", result)
    if result:
        message = result
        return render_template(landing_page, message=message)
    else:
        err_message = "Something went wrong"
        return render_template(landing_page, message=None, err_message=err_message)



# update nutritionist
@app.route('/update_nutritionist', methods=["POST"])
def update_nutritionist():
    updates = request.form.to_dict()
    print("Updates", updates)
    record_id = updates['nutritionist_id']
    print("Record id", record_id)
    result = db.update_record('nutritionist', h.nutritionist_columns, record_id=record_id, update_data=updates, connection=connection)
    print("RESULT", result)
    if result:
        message = result
        return render_template(landing_page, message=message)
    else:
        err_message = "Something went wrong"
        return render_template(landing_page, message=None, err_message=err_message)

# update fintess data
@app.route('/update_fitness_data', methods=["POST"])
def update_fitness_data():
    updates = request.form.to_dict()
    print("Updates", updates)
    record_id = updates['fitness_data_id']
    print("Record id", record_id)
    result = db.update_record('fitness_data', h.fitness_data_columns, record_id=record_id, update_data=updates, connection=connection)
    print("RESULT", result)
    if result:
        message = result
        return render_template(landing_page, message=message)
    else:
        err_message = "Something went wrong"
        return render_template(landing_page, message=None, err_message=err_message)


# update meal plan
@app.route('/update_meal_plan', methods=["POST"])
def update_meal_plan():
    updates = request.form.to_dict()
    print("Updates", updates)
    record_id = updates['meal_plan_id']
    print("Record id", record_id)
    result = db.update_record('meal_plan', h.meal_plan_columns, record_id=record_id, update_data=updates, connection=connection)
    print("RESULT", result)
    if result:
        message = result
        return render_template(landing_page, message=message)
    else:
        err_message = "Something went wrong"
        return render_template(landing_page, message=None, err_message=err_message)


# update patient
@app.route('/update_patient', methods=["POST"])
def update_patient():
    updates = request.form.to_dict()
    print("Updates", updates)
    record_id = updates['patient_id']
    print("Record id", record_id)
    result = db.update_record('patient', h.patient_columns, record_id=record_id, update_data=updates, connection=connection)
    print("RESULT", result)
    if result:
        message = result
        return render_template(landing_page, message=message)
    else:
        err_message = "Something went wrong"
        return render_template(landing_page, message=None, err_message=err_message)


# run query
@app.route('/run_query', methods=['POST'])
def run_query():
    query = request.form.get('query')
    print(query)

    results = db.run_sql_query(query, connection)

    if results:
        results = h.format_data_as_html_table(results)
        message = "Query Ran Successfully"
        return render_template(landing_page, message=message, err_message=None, query_result=results)
    else:
        err_message = "Query did not run successfully"
        return render_template(landing_page, message=None, err_message=err_message)



if __name__== '__main__':
    app.run(debug=True)