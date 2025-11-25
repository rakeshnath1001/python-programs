# create account class with 2 attributes- balance & account no. Create methods for debit,credit & printing the balance

class Account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no= acc


    #debit method
    def debit(self,amount):
        self.balance -= amount
        print("rs", amount, "was debited")
        print("total balance=", self.get_balance())


    #credit method
    def credit(self,amount):
     self.balance += amount  
     print("rs",amount, "was credited")
     print("total balance=", self.get_balance())


    def get_balance(self):
     return self.balance
        
     
#object created and method calling
acc1=Account(100000,12345)
acc1.debit(500)