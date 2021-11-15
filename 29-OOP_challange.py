class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,value):
        print('Deposite Accepted')
        self.balance = self.balance + value
        return self.balance

    def withdraw(self,value1):
        if self.balance >= value1:
            self.balance =  self.balance - value1
            print('Withdraw Succesful')
        else:
            print('Sorry, not enough funds!')
        return self.balance
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: {self.balance} '

ac1 = Account('Marcin', 1000)

print(ac1.deposit(100))
print(ac1.withdraw(100))

print(ac1)
