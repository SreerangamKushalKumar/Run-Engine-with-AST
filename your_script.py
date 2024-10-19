from flask import Flask, request, jsonify, render_template
from rule_handler import create_rule, evaluate_rule  # Updated import
from db_setup import create_table, insert_rule

app = Flask(__name__)

# Ensure the database is set up
create_table()

# Simple route to serve the UI
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to evaluate rules
@app.route('/evaluate', methods=['POST'])
def evaluate():
    # Get form data from the UI
    user_data = {
        'age': int(request.form['age']),
        'department': request.form['department'],
        'salary': int(request.form['salary']),
        'experience': int(request.form['experience'])
    }

    # Example rule string
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    
    # Parse and evaluate the rule
    rule_ast = create_rule(rule_string)
    result = evaluate_rule(rule_ast, user_data)
    
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
