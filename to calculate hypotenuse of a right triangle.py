import math
Base=float(input("Enter the base : "))
height=float(input("Enter the height : "))
c=math.pow(Base,2)+pow(height,2)
print(f"the hypothenuse of a trinagle is {round(math.sqrt(c),2)}")