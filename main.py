

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance = self.balance - amount
            self.withdrawl_fee()

    def withdrawl_fee(self):
        self.balance -= 1

    # def transfer_to(self, amount, owner):
    #     if amount > self.balance:
    #         print("Insufficient funds")
    #     else:


    def print_account_info(self):
        print(f"The balance of {self.owner} is ${self.balance}")


    def __str__(self):
        return f"Owner:{self.owner}, Balance:{self.balance}"

ba = BankAccount("Hazem Farra", 500)

ba.deposit(100)

ba.withdraw(150)

print(ba)

