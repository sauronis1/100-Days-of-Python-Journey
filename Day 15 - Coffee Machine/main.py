#TODO: create a function that prompts the user
#TODO: create a function that will turn the machine off - put the whole code in a while loop
#TODO: create a "report" function that will display the available resources,
#I reckon that will need a dictionary with the resources
#TODO: a function that checks if there are enough resources
#TODO: a function that counts the coins
#TODO: a function that says whether the transaction was sufficient


from menu import MENU
from art import logo


resources = {
    "Water" : 300,
    "Milk" : 200,
    "Coffee" : 100,
}


finances = {
    "Money" : 5,
}


def what_would_you_like():
    order = input("What would you like? (espresso/latte/cappuccino) ")
    return order


def get_necessary_ingredients(item):
    water_needed = MENU[item]["ingredients"]["water"]
    coffee_needed = MENU[item]["ingredients"]["coffee"]
    if item != "espresso":
        milk_needed = MENU[item]["ingredients"]["milk"]
    else:
        milk_needed = 0
    necessary_ingredients = [water_needed, milk_needed, coffee_needed]
    return necessary_ingredients


def report():
    print(f'''
    Water: {resources["Water"]}ml
    Milk: {resources["Milk"]}ml
    Coffee: {resources["Coffee"]}g
    Money: ${finances["Money"]}
''')


def report_in_list():
    resources_owned_list = []
    for key in resources:
        resources_owned_list.append(resources[key])
    return resources_owned_list


def check_resources(item):
    resources_needed = get_necessary_ingredients(item)
    resources_owned = report_in_list()
    for i in range(3):
        if resources_needed[i] > resources_owned[i]:
            print("Sorry, we do not have enough resources. Call for a technician.")
            return False
        else:
            return True


def taking_coins(item):
    money_necessary = MENU[item]["cost"]
    print(f"(A {item} costs ${money_necessary}.)")
    not_paid_for = True
    while not_paid_for:
        quarters_taken = int(input("How many quarters? "))
        dimes_taken = int(input("How many dimes? "))
        nickles_taken = int(input("How many nickles? "))
        pennies_taken = int(input("How many pennies? "))
        money_taken = quarters_taken*0.25 + dimes_taken*0.10 + nickles_taken*0.05 + pennies_taken*0.01
        money_taken_rounded = round(money_taken, 2)
        if money_taken_rounded < 0:
            print("Really? That's the path you've chosen in your life? Trying to steal from a coffee machine?")
        elif money_taken_rounded < money_necessary:
            print("Insufficient funds. Your money has been refunded.")
        elif money_taken_rounded == money_necessary:
            print(f"(You put in ${money_taken_rounded}.)")
            not_paid_for = False
        elif money_taken_rounded >= money_necessary:
            print(f"(You put in ${money_taken_rounded}.)")
            print(f"Here is ${round(money_taken_rounded-money_necessary, 2)} in change.")
            not_paid_for = False


def deduct_resources_and_add_money(item):
    used_ingredients = get_necessary_ingredients(item)
    i = 0
    for key in resources:
        resources[key] -= used_ingredients[i]
        i += 1
    finances["Money"] += MENU[item]["cost"]


def maintenance():
    maintenance_not_over = True
    while maintenance_not_over:
        maintenance_command = input("Hello, technician. What would you like to do? ")
        if maintenance_command == "report":
            report()
            maintenance_not_over = more_maintenance_question()
        elif maintenance_command == "add water":
            add_ingredient("water")
            maintenance_not_over = more_maintenance_question()
        elif maintenance_command == "add milk":
            add_ingredient("milk")
            maintenance_not_over = more_maintenance_question()
        elif maintenance_command == "add coffee":
            add_ingredient("coffee")
            maintenance_not_over = more_maintenance_question()


def more_maintenance_question():
    do_more_maintenance = input("Would you like to do some more maintenance? Type 'y' or 'n': ").lower()
    if do_more_maintenance == "y":
        return True
    else:
        return False
    
    
def add_ingredient(added_ingredient):
    how_much = int(input(f"How much {added_ingredient} would you like to add? "))
    if how_much == 0:
        print("You really think you're so bloody funny then?")
    elif how_much < 0:
        print("What, you want to steal from the coffee machine?")
    else:
        if added_ingredient == "water":
            print("Pouring in some water... ")
            resources["Water"] += how_much
        elif added_ingredient == "milk":
            print("Pouring in some milk...")
            resources["Milk"] += how_much
        elif added_ingredient == "coffee":
            print("Adding some coffee beans...")
            resources["Coffee"] += how_much
            
            
def operate_coffee_machine():
    print(logo)

    not_turned_off = True
    while not_turned_off:
        command = what_would_you_like()
        if command == "maintenance":
            maintenance()
        elif command == "turn off":
            not_turned_off = False
        elif command == "espresso" or command == "latte" or command == "cappuccino":
            should_ask_for_coins = check_resources(command)
            if should_ask_for_coins:
                taking_coins(command)
                deduct_resources_and_add_money(command)
                print(f"Here is your {command} ☕, please enjoy!")


operate_coffee_machine()
