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

balance = 0
def resource_check(drink, resource, total):
    if resource["water"] < MENU[drink.lower()]["ingredients"]["water"]:
        return "water"
    elif resource["milk"] < MENU[drink.lower()]["ingredients"]["milk"]:
        return "milk"
    elif resource["coffee"] < MENU[drink.lower()]["ingredients"]["coffee"]:
        return "coffee"
    elif total < MENU[drink.lower()]["cost"]:
        return 1
    else:
        return 0


def calculate_change(total, drink):
    return round(total - MENU[drink.lower()]["cost"],2)

def resource_use(drink,resource):
    resource["water"] -= MENU[drink.lower()]["ingredients"]["water"]
    resource["milk"] -= MENU[drink.lower()]["ingredients"]["milk"]
    resource["coffee"] -= MENU[drink.lower()]["ingredients"]["coffee"]

continued = True

while continued:
    type_drink = input("What kind of drink would you like: espresso, latte, cappuccino? ")
    if type_drink.lower() == "report":
        print("Report:")
        print(f'Water: {resources["water"]}mL')
        print(f'Milk: {resources["milk"]}mL')
        print(f'Coffee: {resources["coffee"]}mL')
        print(f"Money: ${balance}")
    elif type_drink.lower() == "off":
        print("Good Bye!")
        continued = False
    else:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        total = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
        supply = resource_check(type_drink, resources, total)
        if supply == 0:
            change = calculate_change(total, type_drink)
            print(f"Here is your {type_drink}.")
            print(f"And your change of ${change}.")
            balance = balance + total - change
            resource_use(type_drink,resources)
        elif supply == 1:
            print(f"Sorry not enough money. Your total of ${total} has been refunded.")
            continued = False
        else:
            print(f"Sorry not enough {supply}. Your total of ${total} has been refunded.")
            continued = False
