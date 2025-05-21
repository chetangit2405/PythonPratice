from abc import ABC, abstractmethod
from datetime import datetime

class BankAccount(ABC):
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(balance)
        self.transactions = []  # List to track all transactions

    @abstractmethod
    def calculate_interest(self):
        pass

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.\n")
            return
        self.balance += amount
        self.log_transaction("Deposit", amount)
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.\n")
            return
        if amount > self.balance:
            print("Insufficient balance.\n")
            return
        self.balance -= amount
        self.log_transaction("Withdrawal", amount)
        print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}\n")

    def log_transaction(self, transaction_type, amount):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"{timestamp} - {transaction_type}: ₹{amount}")

    def print_summary(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name  : {self.holder_name}")
        print(f"Balance      : ₹{self.balance}")
        print("Recent Transactions:")
        for t in self.transactions[-5:]:  # Show last 5 transactions
            print(f"  {t}")
        print()

    @staticmethod
    def is_valid_balance(balance_value):
        return float(balance_value) >= 0


class SavingsAccount(BankAccount):
    @classmethod
    def from_string(cls, string_value):
        _, account_number, holder_name, balance = string_value.split("|")
        return cls(account_number, holder_name, balance)

    def calculate_interest(self):
        return self.balance * 0.04


class CurrentAccount(BankAccount):
    @classmethod
    def from_string(cls, string_value):
        _, account_number, holder_name, balance = string_value.split("|")
        return cls(account_number, holder_name, balance)

    def calculate_interest(self):
        return 0


# ✅ Test
acc1 = SavingsAccount.from_string("Savings|101|Chetan|5000")
acc2 = CurrentAccount.from_string("Current|102|Mamatha|7000")

print("Interest:")
print(acc1.calculate_interest())  # 200.0
print(acc2.calculate_interest())  # 0
print()

# Transactions
acc1.deposit(1000)
acc1.withdraw(300)
acc1.withdraw(9999)  # Should show insufficient funds
acc1.deposit(-200)   # Invalid amount

acc2.deposit(2000)
acc2.withdraw(1000)

# Summaries
acc1.print_summary()
acc2.print_summary()

# Validations
print(BankAccount.is_valid_balance(1000))       # True
print(BankAccount.is_valid_balance(-500))       # False