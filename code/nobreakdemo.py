

print('Calculate square roots and enter zero to quit')
x=1
while x!=0:
    x = float(input("Enter a positive number: "))
    if x>0:
        print('the square root of x is',x**0.5)
    elif x<0:
        print("you were supposed to enter positive numbers!!")


print('done')