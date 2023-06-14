## while loops

The syntax of a while loop is
``` python
while TEST:
    STATEMENTS
```

A while loop is evaluated by first evaluating the TEST
if it evaluates to True, then the STATEMENTS are evaluated
and it repeats the process by evaluating the TEST again, etc.

if the TEST evaluates to a False value, then it skips the
statements and the while loops is complete.

### the ```break``` statement
Inside a loop, one can use the ```break``` statement to end the loop.
In general though it is better to use the TEST to end the loop rather
than including a break statement
e.g.
``` python
print('Calcuate square roots and enter zero to quit')
while True:
    x = float(input("Enter a positive number: "))
    if x<=0:
        print("you were supposed to enter positive numbers!!")
        break;
    print('the square root of x is',x**0.5)
```

How would you rewrite this without the break?

### the ```continue``` statement
The ```continue``` statement appearing in a loop, causes Python to skip the
rest of the statements in the loop and to jump back to the TEST.
Here is an example,
``` python
print('Calcuate square roots and enter zero to quit')
while True:
    x = float(input("Enter a positive number: "))
    if x<0:
        print("you were supposed to enter positive numbers!!")
        continue;
    elif x==0:
        break
    print('the square root of x is',x**0.5)
```

How does this differ from the previous program?
