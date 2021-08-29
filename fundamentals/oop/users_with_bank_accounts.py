class User:
    all_user_accounts = []
    def __init__(self, name, last_name, email, account_name):
        self.name = name
        self.email = email
        self.last_name = last_name
        self.account = BankAccount(.02, 0, account_name)
        User.all_user_accounts.append(self)
        # print(f"Name:        {self.name}")
        # print(f"Last Name:   {self.last_name}")
        # print(f"E-mail:      {self.email}")
        # print(f"Account Bal: {self.account_balance}")
        # print()
    # def make_deposit(self, amount):
    #     self.account_balance += amount
    #     return self
    # def make_withdrawal(self, amount):
    #     self.account_balance -= amount
    #     return self
    # def transfer_money(self, name, amount):
    #     self.account_balance -= amount
    #     name.account_balance += amount
    #     print(f'Transfer from {self.name} to {name.name} of ${amount}')
    #     print(f"The New Balance of {self.name} is ${self.account_balance}")
    #     print(f"The New Balance of {name.name} is ${name.account_balance}")
    #     return self
    # def display_user_balance(self):
    #     print(f"The Balance of {self.name} is ${self.account_balance}")
    #     return self

class BankAccount:
# don't forget to add some default values for these parameters!
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, int_rate, balance, account_name): 
        self.int_rate = int_rate
        self.balance = balance
        self.account_name = account_name
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
        print(f"Account: {self.account_name}")
        print (f"Balance: ${self.balance}")
        print (f"Interest Rate: {self.int_rate}%")
        return self
    # your code here
    def yield_interest(self):
        interest = self.balance * self.int_rate
        self.balance += interest
        return self
    # your code here
    @classmethod
    def display_all_accounts(cls):
        for i in cls.all_accounts:
            print(f"Account: {i.account_name}\n Balance: ${i.balance}\n Interest Rate: {i.int_rate}%")

checkings1 = User('John', 'Appleseed', 'john_boy@icloud.com', 'checkings1')
checkings2 = User('Victor', 'Ozone', 'coolguyvic@yahoo.com', 'checkings2')
checkings3 = User('Alejandra', 'Silva', 'TooCool4School@gmail.com', 'checkings3')
savings1 = User('John', 'Appleseed', 'john_boy@icloud.com', 'savings1')
BankAccount.display_all_accounts()
checkings1.account.deposit(500)
savings1.account.deposit(1000000)
checkings1.account.display_account_info()
savings1.account.display_account_info()