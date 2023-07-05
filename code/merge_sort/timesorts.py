from bubblesort import *
from mergesort import *
from matplotlib import pyplot as plt

print('Enter a number n>0')
print("We'll time how long mergesort and bubblesort take.")
print("Don't try bubble sort with n > 1000, it takes too long")

n = int(input("n> "))
while n>0:
    print('starting mergesort')
    print('n=',n,'mergesort=',MStimetest(n))
    print('starting bubblesort')
    print('bubblesort=',BStimetest(n))
    n = int(input("n> "))
print('bye')
