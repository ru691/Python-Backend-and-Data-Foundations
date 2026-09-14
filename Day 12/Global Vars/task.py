# Modifying Global Scope

enemies = 1


def increase_enemies(x):
    # global enemies #allow local scope to use global scope
    print(f"enemies inside function: {enemies}")
    return x + 1


enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")


