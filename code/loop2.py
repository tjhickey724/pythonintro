import math
n = int(input("enter a whole number: "))

for i in range(n+1):
    print("%4d %8d %10d %12.4f %14.6f" % (i, i**2, i**3, i**(1/3), math.sqrt(i)))