print("Is it odd or even?")
number_to_check = int(input("What number are we checking? "))
remainder_check = number_to_check % 2
if remainder_check == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")