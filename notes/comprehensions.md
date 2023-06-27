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

For example, we can a list of the squares of the numbers from 0 to 100 using
``` python
squares = [x*x for x in range(100)]
print(squares)
```
This is called a mapping transformation as it replaces the list ```[0,1,...,100]```
with the list ```[0,1,4,9,16,...,10000]```, i.e. it simiply square each element in the original list.


and we could generate a list of the divisors of a number n using
``` python
def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]
print(divisors(360))
```

