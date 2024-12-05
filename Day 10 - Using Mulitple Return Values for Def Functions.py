def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

# print format_name with inputs as the variables in the defined function
# don't forget to close the parentheses correctly
print(format_name(input("What is your first name?"), input("What is your last name?")))
# or for pre-defined inputs:
print(format_name("AnGEla", "YU"))

# Can put just a blank return and it will print "none" in this case
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide a valid input. Try again"
        # adding a string after the return in this case reminds the developer that something went wrong and
        # signaling that the code below won't run because the input was invalid and/or blank
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name?"), input("What is your last name?")))