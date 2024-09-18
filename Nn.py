name=input("Hello, what is your name?")
if len(name) < 3:
    print("Name must be at least 3 characters")
    print("Press HOME")
elif len(name)>10:
    print("Name must be maximum of 10 characters")
    print("Press HOME")
else:
    print ("Name looks Good")
    print("Press Enter")
