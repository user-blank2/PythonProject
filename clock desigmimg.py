import time
second=int(input("enter the seconds : "))
for i in range(second,-1,-1):
    time.sleep(1)
    second = i % 60
    minute = int(i/60) % 60
    hour= int(i/ 3600)

    print(f"{hour :02} : {minute:02} : {second:02}")
print("Time Over")