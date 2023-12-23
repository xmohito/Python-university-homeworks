class BankAccount:
    def __init__(self, number, currency, balance, owner):
        self.number = number
        self.currency = currency
        self._balance = balance
        self._owner = owner

    @property
    def balance(self):
        return self._balance

    @property
    def owner(self):
        return self._owner

    @balance.setter
    def balance(self, new_balance):
        self._balance = new_balance

    @owner.setter
    def owner(self, new_owner):
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

    @staticmethod
    def convert_currency(amount, exchange_rate):
        return amount * exchange_rate


account1 = BankAccount('12345', 'PLN', 10000, 'Tony Sosa')
account2 = BankAccount('12345', 'PLN', 100, 'Tony Sosa')
account3 = BankAccount('13579', 'EUR', 800, 'Al Capone')
account4 = BankAccount('54321', 'PLN', 200, 'Frank White')

account2.owner = 'John Smith'
account2.balance = 0
print(account2)

usd_to_euro_conversion = BankAccount.convert_currency(100, 0.85)
print(f"100 USD = {usd_to_euro_conversion} EUR")
