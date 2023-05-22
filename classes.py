# Add these attributes and behaviors to the class Account
# Add attributes deposits and withdrawals in the init method which are empty lists by default and another attribute loan_balance which is zero by default.
class Account:
    def __init__(self,deposits,withdrawls,loan_balance):
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=loan_balance

class Account:
 def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

# Add a method check_balance which returns the account’s balance
def check_balance(self,balance):
    return self.balance


class Account:
 def check_balance(self):
        return self.balance
# Update the deposit method to append each withdrawal transaction to the deposits list. Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
class Account:
 def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})
# Update the withdrawal method to append each withdrawal transaction to the withdrawals list. Each transaction should be in form of a dictionary like like this 
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
class Account:
 def withdrawal(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
# Add a new method  print_statement which combines both deposits and withdrawals into one list and, using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
class Account:
 def print_statement(self):
        for transaction in self.deposits:
            print("deposit - " + str(transaction['amount']))
        for transaction in self.withdrawals:
            print("withdrawal - " + str(transaction['amount']))
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
class Account:
 def borrow_loan(self, amount):
        if (self.loan_balance = 0 and amount > 100 and len(self.deposits))>=10 and amount<=(sum(transaction["amount"] for transaction in self.de))

# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance

# Add a transfer method which accepts two attributes (amount and instance of another account). If the amount is less than the current instance's balance, the method transfers the requested amount from the current account to the passed account. The transfer is accomplished by reducing the current account balance and depositing the requested amount to the passed account.
