name = input("enter your name :")
if len(name)>12:
    print("please enter your a valid name")
elif not name.find(" ") == -1 :
    print("name should not contain any spaces")
elif not name.isalpha():
    print("name should not contain any digit")
else:
    print(f"hello {name}")