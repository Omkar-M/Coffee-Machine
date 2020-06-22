# Write your code here

# Define coffees available with resources needed
espresso = {'coffee': 'espresso', 'water': 250, 'milk': 0, 'beans': 16, 'cost': 4}
latte = {'coffee': 'latte', 'water': 350, 'milk': 75, 'beans': 20, 'cost': 7}
cappuccino = {'coffee': 'cappuccino', 'water': 200, 'milk': 100, 'beans': 12, 'cost': 6}

coffee_list = [espresso, latte, cappuccino]

# Initial machine status.
machine_status = {'money': 550, 'cups': 9, 'beans': 120, 'milk': 540, 'water': 400}


def print_machine_menu():
    print("")
    while True:
        print("Write action (b)uy, (f)ill, (t)ake, (r)emaining, (e)xit):")
        selection = str(input("> ")).strip().lower()
        if selection in ('fill', 'buy', 'take', 'remaining', 'exit',
                         'f', 'b', 't', 'r', 'e'):
            return selection
        else:
            print("Please enter a valid choice")


def print_machine_status():
    print("")
    print("The coffee machine has:")
    print(f'{machine_status["water"]} of water')
    print(f'{machine_status["milk"]} of milk')
    print(f'{machine_status["beans"]} of coffee beans')
    print(f'{machine_status["cups"]} of disposable cups')
    print(f'{machine_status["money"]} of money')


def fill_machine():
    print("Write how many ml of water do you want to add:")
    machine_status['water'] += int(input("> "))

    print("Write how many ml of milk do you want to add:")
    machine_status['milk'] += int(input("> "))

    print("Write how many grams of coffee beans do you want to add:")
    machine_status['beans'] += int(input("> "))

    print("Write how many disposable cups of coffee do you want to add:")
    machine_status['cups'] += int(input("> "))


def buy_coffee_menu():
    print("")
    while True:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back:")
        selection = str(input("> ")).strip().lower()

        if selection in ('back', '1', '2', '3'):
            selection = 0 if selection == 'back' else int(selection)
            break
        else:
            print("Please enter a valid choice")

    if selection > 0:
        buy_a_coffee(selection)


def buy_a_coffee(coffee_type):
    """Check machine has the correct amount for the coffee selected
    if the machine can make the coffee then do and update
    else tell the operator what is too low

    Argument: coffee_type(int): 1 latte, 2 esspresso, 3 cappucino
    """
    if coffee_type not in (1, 2, 3):
        print("Please select a valid coffee")

    selected = coffee_list[coffee_type - 1]
    # Check machines capacity to make the coffee
    print(selected)

    anything_missing = []

    if machine_status['water'] < selected['water']:
        anything_missing.append("water")

    if machine_status['milk'] < selected['milk']:
        anything_missing.append("milk")

    if machine_status['beans'] < selected['beans']:
        anything_missing.append("coffee beans")

    if machine_status['cups'] < 1:
        anything_missing.append("disposable cups")

    if len(anything_missing) > 0:
        output = "Sorry, not enough"
        for i in range(0, len(anything_missing)):
            if i > 0:
                output += ", " + anything_missing[i]
            else:
                output += " " + anything_missing[i]
        print(output + "!")
    else:
        print("I have enough resources, making you a coffee!")
        machine_status['water'] -= selected['water']
        machine_status['milk'] -= selected['milk']
        machine_status['beans'] -= selected['beans']
        machine_status['cups'] -= 1
        machine_status['money'] += selected['cost']


def take_money():
    print("")
    print(f"I gave you ${machine_status['money']}")
    machine_status['money'] = 0


answer = print_machine_menu()

while True:
    if answer in ['exit', 'e']:
        break

    elif answer in ['fill', 'f']:
        fill_machine()

    elif answer in ['buy', 'b']:
        buy_coffee_menu()

    elif answer in ['take', 't']:
        take_money()

    elif answer in ['remaining', 'r']:
        print_machine_status()

    answer = print_machine_menu()
