class BankAccount:
	def __init__(self, int_rate, balance): 
        self.balance = 0
        self.int_rate = 0.01
	def deposit(self, amount):
		self.balance =((self.balance + amount) + self.yield_interest() )
	def withdraw(self, amount):
		if self.balance>=amount:
           self.balance-=amount
        else:
            print("\nsorry, Insufficient balance  ")
            self.balance -= 5
	def display_account_info(self):
		 print("hello your net Available Balance is", (self.balance + self.int_rate))
	def yield_interest(self):
		(self.balance * self.int_rate)
  
elias = BankAccount ("Elias W" , "elias.woldeselassie@gmail.com")
jappy = BankAccount ("jappy assfa" , "jappy_a@gmail.com")

elias.deposit(200)
elias.deposit(400)
elias.deposit(300)
elias.withdraw(1050)
elias.display_account_info()