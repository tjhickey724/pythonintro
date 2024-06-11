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
