from balance import view_balance
from deposit import deposit_amt
from withdraw import withdraw_amt

bal = 0
running = True

while running:
   print("<--------Welcome to the bank--------->\n") 
   print("1. View bal")
   print("2. deposit")
   print("3. withdraw")
   print("4. quit")

   choice = int(input("Enter a choice(1-4) : "))

   if choice == 1:
      view_balance(bal)
   elif choice == 2:
      bal += deposit_amt()
   elif choice == 3:
      bal -= withdraw_amt(bal)
   elif choice == 4:
      running = False
   else:
      print("Incorrect input")
   