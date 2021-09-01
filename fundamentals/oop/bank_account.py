class BankAccount:
# don't forget to add some default values for these parameters!
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    # your code here! (remember, instance attributes go here)
    # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    # your code here
    def withdraw(self, amount):
        if(self.balance > 0) and (self.balance >= amount):
            self.balance -= amount
            return self
    # your code here
    def display_account_info(self):
        print (f"Balance: {self.balance}")
        print (f"Interest Rate: {self.int_rate}")
        return self
    # your code here
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance = interest
        return self
    # your code here
    @classmethod
    def display_all_users(cls):
        for x in cls.all_accounts:
            x.display_account_info()

jon1 = BankAccount(1.25, 150000)
brian1 = BankAccount(1.3, 1500000)
BankAccount.display_all_users()
# jon1.deposit(5000).deposit(100000).deposit(250).withdraw(80000).yield_interest().display_account_info()
# brian1.deposit(10000).deposit(22000).withdraw(1000).withdraw(60000).withdraw(50000).withdraw(50).yield_interest().display_account_info()