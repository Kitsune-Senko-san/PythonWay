"""
For this challenge, create a bank account class that has two attributes:
   - owner
   - balance

and two methods:
   - deposit
   - withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, new_deposit=0):
        print(acc1)
        self.balance += new_deposit
        if new_deposit != 0:
            print("Deposit Accepted, total balance  ->  ${}".format(self.balance))
        else:
            print("There was no deposit")

    def withdraw(self, try_withdraw):
        if self.balance < try_withdraw:
            print("Funds Unavailable! The card doesn't have a sufficient amount (${})".format(try_withdraw))
            print("The card balance has not changed\n")
        else:
            print("Withdrawal Accepted, balance decreases  ->  -${}".format(try_withdraw))
            self.balance -= try_withdraw
            print(acc1, "\n")

    def __str__(self):
        return f"Account owner:    {self.owner}\nAccount balance:  ${self.balance}"


acc1 = Account("Jose", 100)
acc1.deposit(50)
acc1.withdraw(150)


acc1 = Account("Julie", 5000)
acc1.deposit(1000)
acc1.withdraw(6001)


acc1 = Account("Bob", 670)
acc1.deposit()
acc1.withdraw(600)
