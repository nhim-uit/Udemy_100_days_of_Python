# Udemy: Master Python by building 100 projects in 100 days
# Aug 20, 2024
# Day 16 - Coffee Machine OOP
# main.py created by me

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def command(coffee_maker: CoffeeMaker, money_machine: MoneyMachine, menu: Menu, coffee: str):
    if coffee == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        flag = coffee_maker.is_resource_sufficient(menu.find_drink(coffee))
        if flag:
            item = menu.find_drink(coffee)

            while not money_machine.make_payment(item.cost):
                pass

            coffee_maker.make_coffee(item)
        return


def run():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    coffee = input('What would you like to order? (latte/espresso/cappuccino) ')

    while coffee != 'off':
        command(coffee_maker, money_machine, menu, coffee)
        coffee = input('What would you like to order? (latte/espresso/cappuccino) ')


if __name__ == '__main__':
    run()








