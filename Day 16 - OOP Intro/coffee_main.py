from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money_machine = MoneyMachine()
# print(my_money_machine.profit) #-> prints profit from MoneyMachine

my_coffee_machine = CoffeeMaker()
# print(my_coffee_machine.report())

my_coffee_menu = Menu()

# TODO 1: to print report for coffee maker
my_coffee_machine.report()
my_money_machine.report()

# TODO 2: ask user for drink type



question = input(f"What drink would you like: {my_coffee_menu.get_items()}?")
# print(question)
# my_coffee_menu.find_drink(question)



# TODO 3: check if resources available

my_coffee_machine.is_resource_sufficient(question)