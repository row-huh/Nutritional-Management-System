from flask import Flask, render_template, request
import database


app = Flask(__name__)
connection = database.initialize_database()


# landing page
@app.route('/')
def index():
    return render_template('test.html')

@app.route('/write_query')
def write_query():
    #TODO
    ...

@app.route('/submit_food', methods=['POST'])
def submit_food():
    form_data = request.form.to_dict()
    database.insert_food_item(form_data, connection)
    message= "New food item created successfully"
    return render_template('test.html', message=message)



if __name__== '__main__':
    app.run(debug=True)
    
    
    
# insert = "submit_<able_name>"
# delete = "delete_<able_name>"
# update = "update_<able_name>"