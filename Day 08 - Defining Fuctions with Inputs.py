def greeting():
    print("Hello")
    print("How are you?")
    print("I am fine, thanks for asking.")

greeting()

# function allows for input
# parameter is "input_name" in this case - name of the input variable
# argument is "Andilyn" in this case - value of the input variable

def greet(input_name):
    print(f"Hello {input_name}")
    print(f"How are you, {input_name}?")
    print(f"I am fine, thanks for asking, {input_name}.")

greet("Andilyn")

# functions with more than 1 input

def greet_name(name, greeting):
    print(f"{greeting} {name}.")

# positional argument - arguments are in direct relation to the order of the parameters

greet_name("Andilyn", "Hello")
greet_name("Robert", "What's up?")

def greet_location(name, location):
    print(f"Hello {name}!")
    print(f"What is the weather like in {location}?")

# keyword argument - input position doesn't matter, parameters are attached to arguments with "="

greet_location(name = "Andilyn", location = "France")
greet_location(location = "Italy", name = "Roberto")