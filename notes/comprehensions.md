# Comprehensions
Python has a special syntax for creating new lists from old lists (and tuples, sets, and dictionaries).
Since this is such a common operation, having a concise syntax for specifying such transformations
makes code much easier to write and to understand.

## General List Comprehension syntax
``` python
result = [EXPRESSION for VARIABLE in LIST if CONDITION]
```
This creates a list by iterating the VARIABLE through the LIST
and for each VARIABLE value that satisfies the CONDITION,
it evaluates the EXPRESSION and stores it in the result list.

## Mapping
For example, we can a list of the squares of the numbers from 0 to 100 using
``` python
squares = [x*x for x in range(100)]
print(squares)
```
This is called a mapping transformation as it replaces the list ```[0,1,...,100]```
with the list ```[0,1,4,9,16,...,10000]```, i.e. it simiply square each element in the original list.
We could also do this with an accumulation loop
``` python
squares = []
for x in range(100):
    squares.append(x*x)
```

## Filtering
We could generate a list of the divisors of a number n using
``` python
def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]
print(divisors(360))
```
This is called a filtering transformation as it starts with the list ```[1,2,...,n]```
and returns a subset of that list (the d's that divide n evenly).

Likewise, we could do this without comprehensions using an accumulation loop:
``` python
def divisors(n):
    ds = []
    for d in range(1,n+1):
        if n%d==0:
            ds.append(d)
    return ds
print(divisors(360))
```

## Mapping and Filtering
We can combine mapping and filtering
For example the following comprehension returns the squares of all odd numbers less than 100
``` python
odd_squares = [d*d for d in range(100) if d%2==1]
print(odd_squares)
```
which we could write without a comprehension as
``` python
odd_squares = []
for d in range(100):
    if d%2==1:
        odd_squares.append(d*d)
```

The general list comprehension
``` python
result = [EXPRESSION for VARIABLE in LIST if CONDITION]
```
can be replaced by an accumulation loop, but it requires more code:
``` python
result = []
for VARIABLE in LIST:
    if CONDITION:
        result.append(EXPRESSION)
```
where of courses we need to replace VARIABLE, LIST, CONDITION, and EXPRESSION
with the appropriate Python code.


