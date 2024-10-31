#Define the Account class
class Account:
    def __init__(self, account_number: str, account_balance: float, account_holder: str):
        self.account_number = account_number 
        self.account_balance = account_balance
        self.account_holder = account_holder

    def deposit(self, deposit_amount:float):
        deposit_amount = float(input(f"Enter the amount you wish to Deposit: "))
        self.account_balance += deposit_amount
        return(f"Credit: Account Number {self.account_number} has been credited with ${deposit_amount} and Current balance is ${self.account_balance}")
    
    def withdraw(self, withdrawal_amount:float):
        withdrawal_amount =float(input(f"Enter the amount you wish to Withdraw: "))
        if withdrawal_amount <= self.account_balance:
            self.account_balance -= withdrawal_amount
            return(f"Debit: Account Number {self.account_number} has been debited with ${withdrawal_amount} and Current balance is ${self.account_balance}")
        else: 
            return(f"insufficient balance for this transaction, Please fund your account.")
    
    def check_balance(self):
        return(f"Dear {self.account_holder} your current balance is ${self.account_balance}")

## Create multiple accounts
myAccount1 = Account("454300212", 500.50,"Ayomide Amir")
print(myAccount1.deposit(1))
print(myAccount1.withdraw(2))
print(myAccount1.check_balance())



myAccount2 = Account("124567829", 1000.50,"Kaybee Muhammed")
print(myAccount2.deposit(1))
print(myAccount2.withdraw(2))
print(myAccount2.check_balance())

myAccount3 = Account("23789504", 1500.50,"Kester Eze")
print(myAccount3.deposit(1))
print(myAccount3.withdraw(2))
print(myAccount3.check_balance())

