"""
from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    @abstractmethod
    def calculate_interest(self):
        pass

    @staticmethod
    def is_valid_balance(balance_value):
        return float(balance_value) > 0

class SavingsAccount(BankAccount):
    def __init__(self, accountType, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        self.accountType = accountType

    @classmethod
    def from_string(cls, string_value):
        accountType, account_number, holder_name, balance = string_value.split("|")
        return cls(accountType, account_number, holder_name, balance)

    def calculate_interest(self):
        return int(self.balance) * 0.04


class CurrentAccount(BankAccount):
    def __init__(self, accountType, account_number, holder_name, balance):
        super().__init__(account_number, holder_name, balance)
        self.accountType = accountType

    @classmethod
    def from_string(cls, string_value):
        accountType, account_number, holder_name, balance = string_value.split("|")
        return cls(accountType, account_number, holder_name, balance)

    def calculate_interest(self):
        return 0



acc1 = SavingsAccount.from_string("Savings|101|Chetan|5000")
acc2 = CurrentAccount.from_string("Current|102|Mamatha|7000")

print(acc1.calculate_interest())  # 200.0
print(acc2.calculate_interest())  # 0

print(BankAccount.is_valid_balance(1000))   # True
print(BankAccount.is_valid_balance(-500))   # False

print(BankAccount.is_valid_balance(12000.00))   # True
print(BankAccount.is_valid_balance(-1500.00))   # False

"""


from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(balance)

    @abstractmethod
    def calculate_interest(self):
        pass

    @staticmethod
    def is_valid_balance(balance_value):
        return float(balance_value) >= 0


class SavingsAccount(BankAccount):
    @classmethod
    def from_string(cls, string_value):
        _, account_number, holder_name, balance = string_value.split("|") # Here "_" is used to ignore the first variable. 
        return cls(account_number, holder_name, balance)

    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):
    @classmethod
    def from_string(cls, string_value):
        _, account_number, holder_name, balance = string_value.split("|") # Here "_" is used to ignore the first variable.
        return cls(account_number, holder_name, balance)

    def calculate_interest(self):
        return 0


# ✅ Test
acc1 = SavingsAccount.from_string("Savings|101|Chetan|5000")
acc2 = CurrentAccount.from_string("Current|102|Mamatha|7000")

print(acc1.calculate_interest())  # 200.0
print(acc2.calculate_interest())  # 0

print(BankAccount.is_valid_balance(1000))       # True
print(BankAccount.is_valid_balance(-500))       # False
print(BankAccount.is_valid_balance(12000.00))   # True
print(BankAccount.is_valid_balance(-1500.00))   # False