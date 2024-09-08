# logic_functions.py

def and_operation(p, q):
    """
    Logical AND operation.
    :param p: First proposition (boolean)
    :param q: Second proposition (boolean)
    :return: Result of p AND q
    """
    return p and q

def or_operation(p, q):
    """
    Logical OR operation.
    :param p: First proposition (boolean)
    :param q: Second proposition (boolean)
    :return: Result of p OR q
    """
    return p or q

def not_operation(p):
    """
    Logical NOT operation.
    :param p: Proposition (boolean)
    :return: Result of NOT p
    """
    return not p

def implies_operation(p, q):
    """
    Logical IMPLIES operation.
    :param p: First proposition (boolean)
    :param q: Second proposition (boolean)
    :return: Result of p IMPLIES q
    """
    return not p or q

def forall(predicate, domain):
    """
    Universal quantifier: Checks if the predicate is true for all elements in the domain.
    :param predicate: Function that takes an element from the domain and returns a boolean value
    :param domain: List of elements to be checked
    :return: True if the predicate is true for all elements, otherwise False
    """
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """
    Existential quantifier: Checks if the predicate is true for at least one element in the domain.
    :param predicate: Function that takes an element from the domain and returns a boolean value
    :param domain: List of elements to be checked
    :return: True if the predicate is true for at least one element, otherwise False
    """
    return any(predicate(x) for x in domain)
