class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance = self.__balance + amount

    def display_balance(self):
        print("Account Balance:", self.__balance)


account = BankAccount(1000)

account.display_balance()

account.deposit(500)

account.display_balance()