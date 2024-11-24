    # Making a simple tip calculator
    # Attempt #1
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
    # Remember PEMDAS
split = float((bill / people) * ((tip / 100) + 1))
    # I had a hard time putting the split in a f-function and having it round to 2 decimal places, but this works.
print("Each person should pay: ")
print(round(split, 2))

    # Attempt #2
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
split = float((bill / people) * ((tip / 100) + 1))
total = round(split, 2)
    # Didn't put in the dollar sign in the first attempt
print(f"Each person should pay: \n${total}")
