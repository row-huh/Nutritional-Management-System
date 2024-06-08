from flask import Flask, render_template, Response

app = Flask(__name__)

# landing page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/write_query')
def write_query():
    #TODO
    ...

@app.route('/submit', methods=['POST'])
def submit_form():
    return Response('Haha, I GOT YOUR INFORMATION NOW')

if __name__== '__main__':
    app.run(debug=True)