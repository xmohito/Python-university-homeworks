class BankAccount:
    def __init__(self, number, currency, balance, owner):
        self.number = number
        self.currency = currency
        self._balance = balance
        self._owner = owner

    def get_balance(self):
        return self._balance

    def get_owner(self):
        return self._owner

    def set_balance(self, new_balance):
        self._balance = new_balance

    def set_owner(self, new_owner):
        self._owner = new_owner

    def __str__(self):
        return f"Account number: {self.number}\nCurrency: {self.currency}\nBalance: {self._balance}\nOwner: {self._owner}"

    def __len__(self):
        return self._balance

    def __add__(self, other):
        if isinstance(other,
                      BankAccount) and self.number == other.number and self.currency == other.currency and self._owner == other._owner:
            return BankAccount(self.number, self.currency, self._balance + other._balance, self._owner)
        else:
            return "Accounts do not meet the conditions for sending money"


account1 = BankAccount('12345', 'PLN', 10000, 'Tony Sosa')
account2 = BankAccount('12345', 'PLN', 100, 'Tony Sosa')
account3 = BankAccount('13579', 'EUR', 800, 'Al Capone')
account4 = BankAccount('54321', 'PLN', 200, 'Frank White')

# __str__ method test
print(account3)
print("\n")

# __len__ method test
account_len = len(account4)
print(f'Balance: {account_len}')
print("\n")

# __add__ method test
send_money = account1 + account2
print(send_money)
print('-----------------------------------')
send_money = account1 + account3
print(send_money)
print("\n")

# getters and setters test
account2.set_owner('John Smith')
account2.set_balance(0)
print(account2)
