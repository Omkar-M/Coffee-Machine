class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "ready"

    def action(self):
        while self.state == "ready":
            action = input("Write action (buy, fill, take, remaining, exit):\n> ")
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.remaining()
            elif action == "exit":
                break
            else:
                print("Try again!\n")

    @classmethod
    def print_enough(cls):
        print("I have enough resources, making you a coffee!\n")

    def buy(self):
        print()
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n>")
        if coffee == "back":
            return
        else:
            coffee = int(coffee)

        if coffee == 1:
            if self.water >= 250:
                if self.milk >= 0:
                    if self.beans >= 16:
                        self.money += 4
                        self.water -= 250
                        self.beans -= 16
                        self.cups -= 1
                        CoffeeMachine.print_enough()
                    else:
                        print("Sorry, not enough coffee beans!\n")
                else:
                    print("Sorry, not enough milk!\n")
            else:
                print("Sorry, not enough water!\n")

        elif coffee == 2:
            if self.water >= 350:
                if self.milk >= 75:
                    if self.beans >= 20:
                        self.money += 7
                        self.water -= 350
                        self.milk -= 75
                        self.beans -= 20
                        self.cups -= 1
                        CoffeeMachine.print_enough()
                    else:
                        print("Sorry, not enough coffee beans!\n")
                else:
                    print("Sorry, not enough milk!\n")
            else:
                print("Sorry, not enough water!\n")

        elif coffee == 3:
            if self.water >= 200:
                if self.milk >= 100:
                    if self.beans >= 12:
                        self.money += 6
                        self.water -= 200
                        self.milk -= 100
                        self.beans -= 12
                        self.cups -= 1
                        CoffeeMachine.print_enough()
                    else:
                        print("Sorry, not enough coffee beans!\n")
                else:
                    print("Sorry, not enough milk!\n")
            else:
                print("Sorry, not enough water!\n")

        else:
            print("Try again!")

    def fill(self):
        print()
        self.water += int(input("Write how many ml of water do you want to add:\n> "))
        self.milk += int(input("Write how many ml of milk do you want to add:\n> "))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n> "))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n> "))
        print()

    def take(self):
        print()
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def remaining(self):
        print()
        print(f"The coffee machine has:\n"
              f"{self.water} of water\n"
              f"{self.milk} of milk\n"
              f"{self.beans} of coffee beans\n"
              f"{self.cups} of disposable cups\n"
              f"${self.money} of money\n")


coffee1 = CoffeeMachine()
coffee1.action()
