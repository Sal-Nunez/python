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
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def transfer_money(self, name, amount):
        self.account_balance -= amount
        name.account_balance += amount
    def display_user_balance(self):
        print(f"The Balance of {self.name} is {self.account_balance}")

jon1 = User('John', 'Appleseed', 'john_boy@icloud.com')
victor1 = User('Victor', 'Ozone', 'coolguyvic@yahoo.com')
alejandra1 = User('Alejandra', 'Silva', 'TooCool4School@gmail.com')

jon1.make_deposit(50)
jon1.make_deposit(100)
jon1.make_withdrawal(2)
jon1.display_user_balance()
victor1.make_deposit(100000)
victor1.make_deposit(50000)
victor1.make_withdrawal(75000)
victor1.display_user_balance()
alejandra1.make_deposit(500)
alejandra1.make_withdrawal(267)
alejandra1.make_withdrawal(100)
alejandra1.make_withdrawal(267)
alejandra1.display_user_balance()
victor1.transfer_money(alejandra1, 200)
victor1.display_user_balance()
alejandra1.display_user_balance()