# Modifying Global Scope

enemies = 1
enemmies = 1
# this will modify the global code:
def increase_enemies():
    # if you want the function to  reference a variable
    # outside of the function, you have to put "global"
    # in front of the local variable to reference it
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

# this will NOT modify the global code
def increase_enemies(enemy):
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemmies = increase_enemies(enemmies)
print(f"enemies outside function: {enemies}")