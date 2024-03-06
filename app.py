#upto 8th step including 7th step 

import re
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Existing routes for the homepage and form submission
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

# New route for email validation
@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    return jsonify({'is_valid': bool(is_valid)})

if __name__ == '__main__':
    app.run(debug=True)














''' upto  to 7th step :
from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    test_string = request.form['test_string']
    regex_pattern = request.form['regex_pattern']
    matches = re.findall(regex_pattern, test_string)
    return render_template('results.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
    '''
