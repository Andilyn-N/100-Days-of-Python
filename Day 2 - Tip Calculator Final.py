    # Attempt #2
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
split = float((bill / people) * ((tip / 100) + 1))
total = round(split, 2)
    # Didn't put in the dollar sign in the first attempt
print(f"Each person should pay: \n${total}")