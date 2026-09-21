MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01

def money():
    print("Please insert coins.")
    quarter = int(input("Please insert quarters: "))
    quarter_sum = quarters * quarter
    dime = int(input("Please insert dimes: "))
    dime_sum = dimes * dime
    nickle = int(input("Please insert nickles: "))
    nickle_sum = nickles * nickle
    pennie = int(input("Please insert pennies: "))
    pennie_sum = pennies * pennie
    return quarter_sum + dime_sum + nickle_sum + pennie_sum

def check_payment(choice):
    cost = MENU[choice]["cost"]
    user_amount = money()
    if user_amount >= cost:
        change = user_amount - cost
        print(f"Here is ${change:.2f} dollars in change")
        return True, user_amount
    else:
        amount_short_of = cost - user_amount
        print(f"Sorry that is not enough money. You only inserted ${user_amount}. You will need another ${amount_short_of:.2f}. Money refunded")
        return False, user_amount

def check_ingredients(choice):
    if choice in MENU:
        ingredients_cost = MENU[choice]["ingredients"]
        for ingredient in ingredients_cost:
            required = ingredients_cost[ingredient]
            available = resources[ingredient]
            if required > available:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True

def updated_ingredients(choice):
    if choice in MENU:
        required_ingredients = MENU[choice]["ingredients"]
        for ingredient in required_ingredients:
            resources[ingredient] = resources[ingredient] - required_ingredients[ingredient]


def coffeemachine():
    profit = 0
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            break
        elif choice == "report":
            print(f"Water : {resources["water"]}ml")
            print(f"Milk  : {resources["milk"]}ml")
            print(f"Coffee : {resources["coffee"]}g")
            print(f"Money : ${profit:.2f}")
        elif choice in MENU:
            if check_ingredients(choice):
                payment_success, money_inserted = check_payment(choice)
                if payment_success:
                    updated_ingredients(choice)
                    profit += MENU[choice]["cost"]
                    print(f"Total amount inserted is ${money_inserted:.2f}.")
                    print(f"Here is your {choice}🍵. Enjoy!")
        else:
            print("Please enter a valid choice")

coffeemachine()