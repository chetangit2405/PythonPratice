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
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Amount {amount} is deposited. New balance is {self.balance}.\n")
        else:
            print(f"Invalid amount.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def account_details(self):
        print(f"Account details \t\n___________________________\nName\t:{self.holder_name}\nAccount number\t:{self.account_number}\nBalance\t:{self.balance}\n")

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

acc1.account_details()
print(f"Interest : {acc1.calculate_interest()}")  # 200.0
print(f"Interest : {acc2.calculate_interest()}")  # 0

acc1.deposit(1000)
acc1.account_details()
acc1.withdraw(200)
acc1.account_details()

acc2.deposit(1000)
acc2.withdraw(200)

print(BankAccount.is_valid_balance(1000))       # True
print(BankAccount.is_valid_balance(-500))       # False
print(BankAccount.is_valid_balance(12000.00))   # True
print(BankAccount.is_valid_balance(-1500.00))   # False

"""
def Bank_menu():
    
    #load_from_file()
    while True:
        print("1. Add Saving account")
        print("2. Add current account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Display account details")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            update_student()
        elif choice == "6":
            remove_student()
        elif choice == "7":
            sortType = input("On what criteria you want to sort (name / age / marks):")
            orderType = input("Enter sorting order (asc / desc):")
            sort_student(sortType, orderType)
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


"""