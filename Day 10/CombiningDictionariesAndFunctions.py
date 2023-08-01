
# Core Functions

# Addition
def add(n1, n2):
    return n1 + n2

# Subtraction
def subtract(n1, n2):
    return n1 - n2

# Multiplication
def multiply(n1, n2):
    return n1 * n2

# Division
def divide(n1, n2):
    return n1 / n2

# Dictionary
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What is the first number?: "))

num2 = int(input("What is the second number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

