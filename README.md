# Rule Engine with Abstract Syntax Tree (AST)

![Screenshot 2024-10-19 182638](https://github.com/user-attachments/assets/539bfdae-7355-4842-8c09-0d391b33f35e)

Develop a simple 3-tier rule engine application(Simple UI, API and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend etc.The system can use Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic creation,combination, and modification of these rules.

# Objective
- User Eligibility: Determine if users meet certain criteria based on attributes.
- Rule Management: Create, combine, evaluate, and modify rules using AST.
- Data Storage: Efficiently store rules and metadata.
# Features
- Rule Creation: Create rules using a string representation that gets converted into an AST.
- Combine Rules: Merge multiple rules into a single AST for efficient evaluation.
- Rule Evaluation: Evaluate combined rules against user attribute data.
- Error Handling: Manage invalid rule strings and data formats gracefully.
- Dynamic Modifications: Modify existing rules and their components.
# Data Structure
- The core data structure used to represent the AST is defined as follows:

```python
class Node:
    def __init__(self, type: str, left=None, right=None, value=None):
        self.type = type  # "operator" for AND/OR, "operand" for conditions
        self.left = left  # Reference to another Node (left child)
        self.right = right  # Reference to another Node (right child for operators)
        self.value = value  # Optional value for operand nodes (e.g., number for comparisons)
```
# Data Storage
- The choice of database for storing the rules and application metadata can vary based on project requirements. Here’s an example schema using a relational database (e.g., PostgreSQL):

Schema
Rules Table
id: INTEGER PRIMARY KEY
rule_string: TEXT NOT NULL
created_at: TIMESTAMP DEFAULT CURRENT_TIMESTAMP
Sample Rule Entries
id	rule_string	created_at
1	"((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"	2023-10-01 12:00:00
2	"((age > 30 AND department = 'Marketing')) AND (salary > 20000 OR experience > 5)"	2023-10-02 12:00:00
API Design
Functions
create_rule(rule_string): Converts a rule string into a Node object representing the corresponding AST.

combine_rules(rules): Takes a list of rule strings and combines them into a single AST, optimizing for efficiency.

evaluate_rule(data): Evaluates a given AST against provided user attributes and returns True or False.

# Test Cases
- The following test cases are implemented to verify the functionality:
- 
1) Rule Creation: Create individual rules from examples and verify their AST representation.
2) Rule Combination: Combine example rules and ensure the resulting AST reflects the combined logic.
3) Rule Evaluation: Implement sample JSON data and test the evaluate_rule function for various scenarios.
4)Dynamic Rule Modification: Explore combining additional rules and test the functionality.

# Bonus Features
- Error Handling: Includes error handling for invalid rule strings and data formats.
- Attribute Validation: Validate attributes to ensure they belong to a defined catalog.
- User-defined Functions: Extend the system to support user-defined functions within the rule language for advanced conditions.

Installation
# Clone the repository:

```bash
git clone https://github.com/SreerangamKushalKumar/Run-Engine-with-AST.git
cd Run-Engine-with-AST
```

Install dependencies:

```bash
pip install -r requirements.txt
```
Run the application:

```bash
Copy code
python app.py
```
# Usage
- Access the application through the provided URL (e.g., http://localhost:5000).
- Follow the API documentation to create and evaluate rules.
