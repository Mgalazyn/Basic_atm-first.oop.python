class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,value):
        print('Deposite Accepted')
        return self.balance + value

    def withdraw(self,value1):
        print('Withdraw Succesful')
        return self.balance - value1
    
    def __str__(self):
        return f'Account owner: {self.owner}\nAccount Balance: {self.balance} '

ac1 = Account('Marcin', 1000)

print(ac1.deposit(100))
print(ac1.withdraw(10))

print(ac1)