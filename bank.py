class Bank():

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance

    def withdraw(self,amount):
        if amount > self.balance:
            raiseValueError("Amount exceeded")
        self.balance -= amount
        return self.balance

    def transfer(self,o2,amount):
        self.balance -= amount
        o2.Bank()
        return 
