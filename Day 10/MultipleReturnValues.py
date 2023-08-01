
# Analysis of return and scope

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

    # Print will not be called
        # print(formated_f_name)
# print(format_name("mitch", "andrade"))

print(format_name(
    input("What is your first name? "),
    input("What is your last name? ")
))