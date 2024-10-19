from rule_engine import create_rule, combine_rules, evaluate_rule

def test_create_rule():
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)
    assert ast is not None

def test_evaluate_rule():
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)
    user_data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
    result = evaluate_rule(ast, user_data)
    assert result == True
