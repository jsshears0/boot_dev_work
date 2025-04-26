class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.deposit_amount = amount
        if self.deposit_amount <= 0:
            raise ValueError ("cannot deposit zero or negative funds")
        else:
            self.__balance += self.deposit_amount

    def withdraw(self, amount):
        self.withdraw_amount = amount
        if self.__balance <= self.withdraw_amount:
            raise ValueError ("insufficient funds")
        elif self.withdraw_amount <= 0:
            raise ValueError ("cannot withdraw zero or negative funds")
        elif self.__balance <= 0:
            raise ValueError ("cannot withdraw zero or negative funds")
        else:
            self.__balance -= self.withdraw_amount