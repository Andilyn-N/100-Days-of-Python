import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0).capitalize(),
                  s)

def my_function():
    return 3*2
# storing the return into variable "output"
output = my_function()

def format_name(f_name, l_name):
    formatted_f_name = titlecase(f_name)
    formatted_l_name = titlecase(l_name)

    return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("andilyn", "NINNEMAN")

# This will store the string "texttext" as function_1 and can be used later
def function_1(text):
    return text + text

# This will store the "text" with the first letter capitalized and the rest lower case
def function_2(text):
    return text.title()

# We store the call of the function with the string "HELLO" as the output2 variable,
# then print it to see it
output2 = function_1("HELLO")
print(output2)
# Using function_1's output as the input for function_2
output3 = function_2(function_1("HELLO"))
print(output3)