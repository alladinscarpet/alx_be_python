"""
You will create two Python scripts:
bank_account.py, which contains the BankAccount class,
that encapsulates banking operations
and main-0.py, which interfaces with the class
through command line arguments to perform banking operations.
"""

class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self, amount):
        self.account_balance -= amount

        if self.account_balance < 0:
            self.account_balance += amount
            return False

        return True




    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")