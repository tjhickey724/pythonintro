import math
n = int(input("enter a whole number: "))
for i in range(n+1):
    print("%4d %10d  %12.4f" % (i, i**2, math.sqrt(i)) )
    