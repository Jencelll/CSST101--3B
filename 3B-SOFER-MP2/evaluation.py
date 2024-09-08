# evaluation.py

def evaluate(statement, values):
    """
    Evaluate a logical statement based on given values.
    :param statement: Logical expression as a string (e.g., "p and q")
    :param values: Dictionary mapping propositions to their truth values
    :return: Result of the logical statement evaluation
    """
    # Replace propositions in the statement with their boolean values
    for var, val in values.items():
        statement = statement.replace(var, str(val))
    
    # Evaluate the logical expression
    return eval(statement)
