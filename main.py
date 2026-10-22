from balance import *
from deposit import *
from withdraw import *

bal = 0
running = True

while running:
   print("Welcome to the bank\n") 
   print("1. View bal")
   print("2. deposit")
   print("3. withdraw")
   print("4. quit")

   choice = int(input("Enter a choice(1-4) : "))

   