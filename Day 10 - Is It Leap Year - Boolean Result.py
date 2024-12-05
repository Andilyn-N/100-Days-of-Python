def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    div4math = int(year) % 4
    if div4math != 0:
        return False
    div100math = int(year) % 100
    if div100math != 0:
        return True
    div400math = int(year) % 400
    if div400math == 0:
        return True
    else:
        return False

# insert year into print statement below to check
print(is_leap_year(1903))