from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

dolce_gusto_9001 = CoffeeMaker()
coin_guzzler = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "maintenance":
        dolce_gusto_9001.maintenance(coin_guzzler)
    else:
        drink = menu.find_drink(choice)
        if drink != None:
            if dolce_gusto_9001.is_resource_sufficient(drink) and coin_guzzler.make_payment(drink.cost):
                    dolce_gusto_9001.make_coffee(drink)
