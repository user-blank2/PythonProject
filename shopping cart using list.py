foods=[]
prices=[]
total=0
while True:
    food=input("enter the food you want : ")
    if food.lower() == "q":
        break
    else :
        price =float(input("Enter the price : "))
        foods.append(food)
        prices.append(price)
print("---YOUR CART---")
for x in foods:
    print(x,end=" ")
print()




for price in prices:
    total+=price
print(f"your total price is {total:.2f}")