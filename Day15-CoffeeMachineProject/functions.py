from CONSTANTS import *


def command(storage: dict, coffee: str):
    """
    Run the program based on user's input
    :param storage:
    :param coffee:
    :return:
    """
    if coffee == 'report':
        report(storage)
    else:
        flag = storage_check(storage, coffee)

        if flag:
            coins = calc_coins(storage, coffee)

            while coins - MENU[coffee]['cost'] < 0:
                print('Sorry, there\'s not enough coins. Refunded.')
                coins = calc_coins(storage, coffee)

            charge = coins - MENU[coffee]['cost']

            storage['money'] += MENU[coffee]['cost']
            print(f'Here is ${charge: .2f} in charge.')
            print(f'Here is your {coffee}. Enjoy!')
        return


def report(storage: dict):
    """
    Print the report of storage of ingredients
    :param storage:
    :return:
    """
    print(f"Water: {storage['water']}ml\n"
          f"Milk: {storage['milk']}ml\n"
          f"Coffee: {storage['coffee']}g\n"
          f"Money: ${storage['money']}")


def calc_coins(storage: dict, coffee: str):
    """
    Returns the total calculated from coins inserted
    :param storage:
    :param coffee:
    :return:
    """
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))

    return quarters * QUARTER + dimes * DIME + nickles * NICKLE + pennies * PENNY


def storage_check(storage: dict, coffee: str):
    """
    Updated storage after deducting amount of ingredients needed
    Returns True when order can be made and False otherwise
    :param storage:
    :param coffee:
    :return:
    """
    if storage['water'] < MENU[coffee]['water']:
        print('Sorry there is not enough water.')
        return False
    if storage['coffee'] < MENU[coffee]['coffee']:
        print('Sorry there is not enough coffee.')
        return False
    if coffee == 'espresso':
        if storage['milk'] < MENU[coffee]['milk']:
            print('Sorry there is not enough milk.')
            return False

    storage['water'] -= MENU[coffee]['water']
    storage['milk'] -= MENU[coffee]['milk']
    storage['coffee'] -= MENU[coffee]['coffee']

    return True


def create():
    """
    Create initial storage of ingredients
    :return: dict
    """
    return {
        'water': 300,
        'milk': 200,
        'coffee': 100,
        'money': 0,
    }


def run():
    cmd = input('What would you like? (espresso/latte/cappuccino): ')
    storage = create()

    while cmd != 'off' \
            and storage['water'] != 0 \
            and storage['milk'] != 0 \
            and storage['coffee'] != 0:
        command(storage, cmd)

        if storage['water'] == 0 \
            or storage['milk'] == 0 \
            or storage['coffee'] == 0:
            print('*' * 50)
            report(storage)
            return

        cmd = input('What would you like? (espresso/latte/cappuccino): ')

    print('*' * 50)
    report(storage)
