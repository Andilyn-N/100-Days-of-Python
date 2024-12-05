# to document what the function is and what it does
# shows up when you hover over the function name in the code
def format_name(f_name, l_name):
    """Take a first and last name and
    format it to return the title case version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")

length = len(formatted_name)