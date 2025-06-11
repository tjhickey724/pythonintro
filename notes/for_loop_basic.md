# for loops

An indexed for loop lets you repeat a sequence of statements multiple times
with different values of some specified variable.

## The simplest indexed for loop
The simplest for loop has the following form:
``` python
for V in range(N):
    statements
```
and this will evaluate the statements N times for V=0, V=1, ... , V=N-1
So it is equivalent to the following code:
``` python
V=0
statements
V=1
statements
...
V=N-1
statements
```

For example, 
``` python
for i in range(3):
    print('i=',i)
    print('i*i=',i*i)
```
 is the same as
``` python
i=0
print('i=',i)
print('i*i=',i*i)
i=1
print('i=',i)
print('i*i=',i*i)
i=2
print('i=',i)
print('i*i=',i*i)
```

We can replace the for loop with an equivalent while loop as follows:
``` python
i=0
while i<4:
    print('i=',i)
    print('i*i=',i*i)
    i+=1
print('Done')
```

## Iterating over a list
You can also use a for list to iterate over a list of Python objects
and formatted printing can make the output line up nicely in columns
```
for x in [2,3,5,7,11,13,17,19]:
   print(f"{x:6d} {x**2:6d} {x**0.5:6.2f}")
```
and here is another example
```
names = "abe ben carl diane ed fatima guy 山下　ひとし　安子".split()
for name in names:
   print(f"{name:8} has {len(name):3} letters")
```  

## Nested Loops
When processing a table of data one often uses nested loops, the outer one for the row, the inner for column
```
for row in range(5):
  for col in range(3):
     print((row,col),end=" ")
  print()
```
The inner loop might also depend on the outer loop variable:
```
for row in range(5):
  for col in range(row):
     print((row,col),end=" ")
  print()
```
