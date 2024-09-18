print("welcome to savage real estate")
name=input("what is your name?")
print(f"hi, {name}")
print("price of house is $1M")
price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else :
    down_payment=0.2*price
print(f"Make a down payment:${down_payment}")