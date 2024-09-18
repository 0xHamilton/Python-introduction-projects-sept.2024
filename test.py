print("welcome to weight converter app")
name=input("what is your name?")
print(f"hi, {name}")
question=input("input either kg or lb")
weight=int(input("what is your weightin the unit you chose?"))
kg = 1000
lb = 0.45
if question == str('lb'):
    converted_weight = weight * kg
    print(f'your Kg weight is, {converted_weight}')
else:
    converted_weight= weight * lb
    print(f'your lb weight is, {converted_weight}')