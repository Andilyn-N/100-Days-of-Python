logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calc_dict = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# print(calc_dict["*"](4, 8))
# output will print 32

calc_continue = True
running_number = {}
turn_number = 0
initial_num = float(input("What's the first number?\n"))

while calc_continue:
    operation = input("Pick an operation: \n+\n-\n*\n/\n")
    second_num = float(input("What's the next number?\n"))

    answer = calc_dict[operation](initial_num, second_num)

    print(f"{initial_num} {operation} {second_num} = {answer}")

    running_number[turn_number] = answer

    # print(running_number)

    turn_number += 1

    restart_question = input(f"Type 'y' to continue calculating with {answer}, "
                             "or type 'n' to start a new calculation or exit:\n").lower()
    if restart_question == "y":
        initial_num = answer
    elif restart_question == "n":
        continue_question = input("Are you finished calculating? Type 'y' or 'n':\n").lower()
        if continue_question == 'y':
            print("Goodbye.")
            calc_continue = False
        else:
            initial_num = float(input("What's the first number?\n"))
            running_number = {}
            turn_number = 0