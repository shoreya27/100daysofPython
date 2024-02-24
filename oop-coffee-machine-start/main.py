from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
from art import logo
table = PrettyTable()
# print the report of coffee maker

betty = CoffeeMaker()
betty.report()

# checking if the resource is sufficient
# checks the menu
table.field_names = ['Coffee Name', 'cost']
main_menu = Menu()
for menu in main_menu.menu:
    table.add_row([menu.name,
                  menu.cost])
print(logo)
print(table)

# checking the resources sufficient for
# espresso
drink = main_menu.find_drink('espresso')
drink_possible = betty.is_resource_sufficient(drink)
if drink_possible:
    print(f'{drink.name} is Available.')
else:
    print(f'Sorry, {drink.name} is not available currently.')

# Processing coins
ruby = MoneyMachine()
payment = ruby.make_payment(drink.cost)
if payment:
    print("Your payment is successful. Thanks for order")
else:
    print("oops! Didn't go through.")

# betty is making coffee
coffee = betty.make_coffee(drink)