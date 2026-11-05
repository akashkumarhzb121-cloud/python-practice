#A. Encapsulation in more detail
#Consider a bank account. You shouldn't let every part of your program change the balance without validation.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())
'''
Output: 1500

This approach centralizes the balance-update rules and helps prevent invalid operations.
'''