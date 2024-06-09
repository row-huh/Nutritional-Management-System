from flask import Flask, render_template, request

app = Flask(__name__)

# landing page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_query')
def write_query():
    #TODO
    ...

@app.route('/submit_food', methods=['POST'])
def submit_food():
    form_data = request.form.to_dict()
    
    print(form_data)
    message= "New food item created successfully"
    return render_template('index.html', message=message)



if __name__== '__main__':
    app.run(debug=True)
    
    
    
# insert = "submit_<able_name>"
# delete = "delete_<able_name>"
# update = "update_<able_name>"