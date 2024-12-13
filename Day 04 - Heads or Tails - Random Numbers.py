import random

# whole numbers a <= N <= b
# may get a or b.
# random_integer = random.randint(1, 10)
# print(random_integer)

# random floating number between 0.0 <= X < 1.0
# will not get 1.0. may get 0.0
# can multiply by 10, 100, 1000, etc to get non-decimals
# random_0_to_1 = random.random()
# print(random_0_to_1)

#a <= N <= b for a <= b and b <= N <= a for b < a.
# random number between a and b, inclusive of a and b.
# The end-point value b may or may not be included in the range
# depending on floating-point rounding in the expression a + (b-a) * random()
# random_float = random.uniform(1, 10)
# print(random_float)

print("Heads or tails?")
random_integer = random.randint(1, 10)
remaindercheck = random_integer % 2
if remaindercheck == 0:
    print("Heads!")
else:
    print("Tails!")