from main import bal
def withdraw():
    amt = float(input("Enter amount to be withdrawn : "))
    if amt < 0:
        print("invalid amount")
        return 0
    elif amt > bal:
        print(f"your withdrawal amount {amt} exceeds your balance of {bal}")
        return 0
    return amt