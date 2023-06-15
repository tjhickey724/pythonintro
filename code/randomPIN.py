from random import randint

n=int(input('Input a whole number: '))

for x in range (n):
    d = randint(0,9)
    print(d, end="")
print()
