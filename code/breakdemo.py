print('Calcuate square roots and enter zero to quit')
while True:
    x = float(input("Enter a positive number: "))
    if x<=0:
        print("you were supposed to enter positive numbers!!")
        break;
    print('the square root of x is',x**0.5)
print('done')