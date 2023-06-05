# Range
The range generator produces sequence of integers, 
* from a starting value START (default is 0)
* up to but not including a ending value FINISH,
* with a step size STEP (default is 1)

Since it is a generator, if you want to see the values it produces
you need to use the list function.

## range(FINISH)
This form generates integers from 0 to FINISH-1,
for example
``` python
list(range(5)) --> [0,1,2,3,4]
```

## range(START,FINISH)
This is similar, but starts at a specified value START.
For example,
``` python
list(range(3,8)) --> [3,4,5,6,7]
```

### range(START, FINISH, STEP)
This adds a step size which can be positive or negative (but not zero).
For example,
``` python
list(range(3,11,2) --> [3,5,7,9]
list(range(10,0,-2) -> [10.8.6.4.2]
list(range(100,50,-7) -> [93,86,79,72,65,58,51]
```

The range generate is most often used in for loops.
For example,
``` python
for j in range(100,50,-7):
    print(j,end=",")
# which will print
93,86,79,72,65,58,51
```
