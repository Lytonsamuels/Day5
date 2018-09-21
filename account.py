class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = False

    def get_balance(self):
        if not self.status:
            raise valueError("no transaction on a closed account")
        return self.balance

    def open(self):
        self.status = True

    def deposit(self, amount):
        if not self.status:
            raise valueError("cant deposit a negative amount")
            self.balance += amount

    def withdraw(self, amount):
        if not self.status:
            raise valueError("no transaction on a closed account")
        if amount < 0:
            raise valueError("cant withdraw a negative amount")
        if self.balance < amount:
            raise valueError("insufficient funds")
        self.balance -= amount
        return self.balance

    def close(self):
        self.status = false

        