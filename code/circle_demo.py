import math
import math
response='y'
while response=='y':
    r=float(input("enter r: "))
    print('area is', math.pi*r**2)
    print('circumference is', math.pi*2*r)
    response = input("more? (y or n)")
print('bye')
