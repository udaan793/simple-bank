def deposit_amt():
    amt = float(input("Enter amount to be deposited : \n"))
    if amt < 0:
        print("Invalid amount")
        return 0
    return amt
