from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee = CoffeeMaker()
my_menu = Menu()
money = MoneyMachine()

while True:
    what_to_do = input("What would you like? (espresso/latte/cappuccino/): ")
    if what_to_do == "off":
        print("machine is turn off")
        break
    elif what_to_do == "report":
        coffee.report()
    else:
        drink = my_menu.find_drink(what_to_do)
        if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            coffee.make_coffee(drink)












        
    

