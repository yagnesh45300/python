import random # Random  generators variable and value
import sys #system
 
class ATM():
    def __init__(self, name, account_number, balance = 0):   #  access is required to initialize the attributes of the class
        self.name = name
        self.account_number = account_number
        self.balance = balance
         
    def account_detail(self):
        print("\n----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Rs.{self.balance}\n")
         
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()
 
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Rs.{amount} withdrawal successful!")
            print("Current account balance: Rs.", self.balance)
            print()
 
    def check_balance(self):
        print("Available balance: Rs.", self.balance)
        print()
 
    def transaction(self):
        print("""
            TRANSACTION 
        *********************
            Menu:
            1. Account Detail
            2. Check Balance
            3. Deposit
            4. Withdraw
            5. Exit
        *********************
        """)
        
        while True:
            try:                                       # The try block lets you test a block of code for errors.
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:                                      #  The except block lets you handle the error.
                print("Error: Enter 1, 2, 3, 4, or 5 only!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rs.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rs.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print(f"""
                printing receipt..............
          ******************************************
              Transaction is now complete.                         
              Transaction number: {random.randint(10000, 1000000)} 
              Account holder: {self.name.upper()}                  
              Account number: {self.account_number}                
              Available balance: Rs.{self.balance}                    
 
             -------------------------------------
            | Thanks for choosing us as your bank |
            | Visit us again!                     |
             -------------------------------------                 
          ******************************************
          """)
                    sys.exit() # for exit to the program
                 
 
print("*******WELCOME TO BANK OF INDIA*******")
print("\n")
print("----------ACCOUNT CREATION----------")
name = input("Enter your name: ")
account_number = input("Enter your account number: ")
print("Congratulations! Account created successfully......\n")
 
atm = ATM(name, account_number)
 
while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y" and "Y":
        atm.transaction()
    elif trans == "n" and "N":
        print("""
    -------------------------------------
   | Thanks for choosing us as your bank |
   | Visit us again!                     |
    -------------------------------------
        """)
        break
    else:
        print("Wrong command! ")
        print("enter in yes( y or Y) and no(n or N)")