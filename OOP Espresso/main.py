from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
powered = True




while powered:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) \n")
    if choice.lower() == "off":
        powered = False
    elif choice.lower() == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice.lower())
        resource = coffee_maker.is_resource_sufficient(drink)
        if resource:
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)



