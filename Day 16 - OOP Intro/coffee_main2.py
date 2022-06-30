from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
# print(my_money_machine.profit) #-> prints profit from MoneyMachine

my_coffee_machine = CoffeeMaker()
# print(my_coffee_machine.report()) #-> prints report from Coffee Maker

my_coffee_menu = Menu()
# print(my_coffee_menu.get_items()) # -> prints the drink names from menu class

is_on = True

while is_on:
    options = my_coffee_menu.get_items()
    choice = input(f"What drink would you like: {options}?")
    #print(choice)
    if choice == 'report':
        my_coffee_machine.report()
        my_money_machine.report()
    elif choice == 'off':
        is_on = False
    else:
        selected_drink = my_coffee_menu.find_drink(choice)
        if my_coffee_machine.is_resource_sufficient(selected_drink) and my_money_machine.make_payment(selected_drink.cost):
            my_coffee_machine.make_coffee(selected_drink)