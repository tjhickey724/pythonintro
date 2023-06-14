# Accumulation Loops
A very common pattern in Python (and all programming languages) is the accumulation loop.
In which some variable is initialized before the loop and then it is modified during the loop,
e.g. summing a sequence of numbers, or finding the smallest or largest number in a sequence,
or finding the number of words in a sequence of strings, etc.

It has the form
``` python
VARIABLE = INITIAL_VALUE
while TEST:
    STATEMENTS THAT UPDATE THE VARIABLE
```

For example,
``` python
total=0
x = float(input("Enter a poitive number: "))
while x > 0:
    total += x;
    x = float(input("Enter a positive number (0 to step): "))
print('The total is',total)
```

How would we count the number of values entered?

How would be compute the average of the values entered?

How would we find the largest value entered?
