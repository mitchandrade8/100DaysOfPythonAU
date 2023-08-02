
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

# Recursion

def calculator():
    num1 = int(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        #Reusability and using the previous answer ** Chaining 

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
            num1 = answer
        else: 
            should_continue = False
            calculator()
            # Recursion because the function will go find itself and reset 
                # Would explain recursion as reseting to the beginning state: Start of a lifecycle


calculator()