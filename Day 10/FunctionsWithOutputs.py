
# Overview of basic functions:
    # def my_function():
        # Do this
        # Then do this
        # Finally do this

# Overview of funcions with Inputs
    # def my_function(something):
        # Do this with something
        # Then do this 
        # Finally do this

# Final level of functions 

# Example of function with Output

def my_function():
    result = 3 * 2
    return print(result)

my_function()

## Deep Dive Into Functions with Outputs

def format_name(first_Name, last_Name):

    # Convert strings 
    formated_f_name = first_Name.title()
    formated_l_name = last_Name.title()

    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("mitch", "andrade")
print(formated_string)



