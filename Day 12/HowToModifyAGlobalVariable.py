

enemies = 1

def increase_enemies():
    # enemies = 2
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Community will tell you to use global to read or use // but do not modify a global variable in Python
