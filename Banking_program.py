#create a Banking program.
#show balance,deposite,withdraw

def check_balance(balance):
    print(f"Your Balance is N{balance:.2f}")
def deposit():
    Amount=float(input("Enter Amount you want to deposit"))

    if Amount<0:
        print("Enter a Valid Amount")
        return 0 
    else:
        return Amount
def withdraw(balance):
    Amount=float(input("Enter Amount to withdraw"))
    if Amount>balance:
        print("insurficient Funds")
        return 0
    elif Amount<0:
        print("Invalid Amount")
        return 0
    else:
        return Amount

def main():
    balance=0 
    is_running=True

    while is_running:
        print("welcome to Zenith Bank PLC")
        print("select the task you want to perform")
        print("1. check Balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")

    choice=int(input("Enter your choice selecting any from 1-4"))
    if choice== 1:
        check_balance(balance)
    elif choice== 2:
        balance += deposit()
    elif choice== 3:
        balance-=withdraw(balance)
    elif choice== 4:
        print("Thank you for Banking with us")
        is_running=False
    else:
        print("The Option you Entered is not Valid")

print("Thank you for Banking with us")
print("Have a nice Day!")

if __name__=='__main__':
    main()