class BankAccount():
    def __init__(self,username, email, int_rate, balance): 
        self.name = username
        self.email = email        
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
    
elias = BankAccount("Elias W" , "elias.woldeselassie@gmail.com", 1.5 , 0)
jappy = BankAccount("jappy assfa" , "jappy_a@gmail.com", 1.5 , 0)

elias.deposit(200).deposit(400).deposit(300).withdraw(10500).display_account_info()

jappy.deposit(4000).deposit(200).withdraw(3000).withdraw(150).withdraw(200).withdraw(2500).display_account_info()