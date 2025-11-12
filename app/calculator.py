def add(a, b):
    """Additionne deux nombres"""
    return a + b


def subtract(a, b):
    result = a - b
    return result


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return a / b


def unused_function():
    # Cette fonction n'est pas utilisée
    x = 1
    y = 2
    return x + y


class Calculator:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value
