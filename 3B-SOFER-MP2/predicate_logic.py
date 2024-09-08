# predicate_logic.py

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
