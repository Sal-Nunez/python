class User:
    def __init__(self, name, last_name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
        self.last_name = last_name
        # print(f"Name:        {self.name}")
        # print(f"Last Name:   {self.last_name}")
        # print(f"E-mail:      {self.email}")
        # print(f"Account Bal: {self.account_balance}")
        # print()
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def transfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount
        print(f'Transfer from {self.name} to {name.name} of ${amount}')
        print(f"The New Balance of {self.name} is ${self.account_balance}")
        print(f"The New Balance of {name.name} is ${name.account_balance}")
        return self
    def display_user_balance(self):
        print(f"The Balance of {self.name} is ${self.account_balance}")
        return self

jon1 = User('John', 'Appleseed', 'john_boy@icloud.com')
victor1 = User('Victor', 'Ozone', 'coolguyvic@yahoo.com')
alejandra1 = User('Alejandra', 'Silva', 'TooCool4School@gmail.com')

jon1.make_deposit(50).make_deposit(100).make_withdrawal(2).display_user_balance()
alejandra1.make_deposit(500).make_withdrawal(267).make_withdrawal(100).make_withdrawal(267).display_user_balance()
victor1.make_deposit(100000).make_deposit(50000).make_withdrawal(75000).display_user_balance().transfer_money(alejandra1, 200)