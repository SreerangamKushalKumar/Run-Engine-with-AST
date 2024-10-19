# rule_handler.py

def create_rule(rule_string):
    # Your logic for creating a rule (parsing the rule_string)
    ast = []  # Replace with actual logic to create the AST
    return ast

def evaluate_rule(ast, user_data):
    # Your logic for evaluating the AST against user data
    if ast is None:
        return None
    
    # Simple evaluation logic (customize this as per your requirements)
    for condition in ast:
        # Example condition check logic (simplified)
        if not evaluate_condition(condition, user_data):
            return False
    return True

def evaluate_condition(condition, user_data):
    # Implement the logic to evaluate a single condition
    # Return True or False based on user data
    # This is a placeholder for actual condition logic
    return True  # Replace with actual evaluation
