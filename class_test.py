class Calculate(object):
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money
    def deposit(newamount):
        self.money = self.money+newamount
        return self.money
    def withdraw(deductamount):
        if self.money >= deductamount:
            self.money = self.money-deductamount
        return self.money
    def __str__(self):
        return "Calculate[name= " +self.name + \
               " age= " + self.age + \
               " money= " + self.money + \
               "]"


if __name__ == "__main__":
    banker1 = Calculate('poo','23','400')
    banker1.deposit('500')
    banker1.withdraw('200')
    print banker1
    
        
        
