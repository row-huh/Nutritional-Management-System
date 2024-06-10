from flask import Flask, render_template, request
import database as db
import database_setup as dbsetup
import helper as h

app = Flask(__name__)
connection = dbsetup.initialize_database()


landing_page = 'dashboard.html'

# landing page
@app.route('/')
def index():
    all_patients = db.fetch_patients(connection)
    all_patients = h.format_data_as_html_table(all_patients)
    return render_template(landing_page, message=None, all_patients=all_patients)


# insert food item
@app.route('/submit_food', methods=['POST'])
def submit_food():
    form_data = request.form.to_dict()
    db.insert_food_item(form_data, connection)
    message= "New food item created successfully"
    index(message=message)


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
    db.insert_meal_plan(form_data, connection)
    message= "New meal_plan created successfully"
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


# update details


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