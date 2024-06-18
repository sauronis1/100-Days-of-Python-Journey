class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

##############################################################

    def add_resources(self, ingredient):
        how_much = int(input(f"How much {ingredient} do you want to add?"))
        if how_much <= 0:
            print("Very funny.")
        else:
            print(f"Adding some {ingredient}...")
            self.resources[ingredient] += how_much


    def maintenance(self, money_machine):
        what_to_do = input("Hello, technician. What would you like to do?")
        ingredient = ""
        if what_to_do == "report":
            self.report()
            money_machine.report()
        elif what_to_do == "add water":
            ingredient = "water"
            self.add_resources(ingredient)
        elif what_to_do == "add milk":
            ingredient = "milk"
            self.add_resources(ingredient)
        elif what_to_do == "add coffee":
            ingredient = "coffee"
            self.add_resources(ingredient)
        else:
            print("I'm sorry, I do not understand this command.")
