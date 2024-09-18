print("welcome to weight converter app")
name=input("what is your name?")
print(f"hi, {name}")
weight=int(input("what is your weight?"))
unit=input("K(g) or L(bs? :")
if unit.upper()== "L":
    converted=weight * 0.45
    print(f"you are {converted} kilos")
else:
    converted=weight// 0.45
    print(f"you are {converted} pounds")