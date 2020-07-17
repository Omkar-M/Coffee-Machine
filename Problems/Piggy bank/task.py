class PiggyBank:
    # create __init__ and add_money methods
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            quotient = self.cents / 100
            remainder = self.cents % 100
            self.dollars += int(quotient)
            self.cents = remainder


# bank = PiggyBank(1,1)
# bank.add_money(0,99)
# print(bank.dollars, bank.cents)
