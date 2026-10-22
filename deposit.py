def deposit():
    amt = float(input("Enter amount to be deposited : "))
    if amt < 0:
        print("Invalid amount")
        return 0
    return amt
