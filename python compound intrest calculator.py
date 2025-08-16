initial_amount=0
intrest =0
time=0
while True:
    initial_amount=float(input("enter your initial amount:"))
    if initial_amount <0:
        print("enter a proper intrest value : ")
    else:
        break

while intrest<=0:
    intrest=float(input("enter your intrest amount :"))
    if intrest<=0:
        print("enter a proper intrest: ")

while time<=0:
    time=int(input("enter your time :"))
    if time <=0:
        print("enter a proper time : ")

total = initial_amount*pow((1 + intrest/100),time)
print(f"balance after {time} year : {total:.2f}")