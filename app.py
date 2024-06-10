from flask import Flask, render_template, request
import database as db
import database_setup as dbsetup


app = Flask(__name__)
connection = dbsetup.initialize_database()


landing_page = 'dashboard.html'

# landing page
@app.route('/')
def index():
    return render_template(landing_page)


# insert food item
@app.route('/submit_food', methods=['POST'])
def submit_food():
    form_data = request.form.to_dict()
    db.insert_food_item(form_data, connection)
    message= "New food item created successfully"
    return render_template('test.html', message=message)


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



@app.route('/write_query')
def write_query():
    #TODO
    ...




if __name__== '__main__':
    app.run(debug=True)