class BankAccount:
    def __init__(self,int_rate, balance):  
        self.balance = balance
        self.int_rate = int_rate
   
    def deposit(self, amount):
        self.balance +=amount
        return self

    def withdraw(self, amount):
     if self.balance>=amount:
        self.balance-=amount
     else:
        print("\nsorry, Insufficient balance  ")
        self.balance -= 5
        return self
    def display_account_info(self):
        print("Account : $" + str(self.balance) +
             "\n" + "Interest rate:", int(self.balance) * int(self.int_rate) / 100 ,
             "\n" + "Total Account balance:", int(self.balance) + int(self.balance) * int(self.int_rate) / 100)
        
    def yield_interest(self):
        self.balance =+ self.balance * self.int_rate / 100


class User:
    # updated methods
    
    def __init__(self, username,email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
    	self.account += amount
    def make_withdrow(self, amount):
        if self.account>=amount:
           self.account-=amount
        else:
            print("\nsorry, Insufficient balance  ")
    def display_user_balance(self):
        print("hello",self.name, "your net Available Balance is", self.account)
    def transfer_money(self, from_account, to_account , amount):
        from_account.make_withdrow(amount)
        to_account.make_deposit(amount)
  

