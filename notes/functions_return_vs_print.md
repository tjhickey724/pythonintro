# Using return vs using print in a function

There are two ways that a function can produce a useful value
1. it can contain a print statement that display the value on the terminal
2. it can contain a return statement that returns the value

Usually, we want to have it return a value which we can then print later.

Let's look at a simple example - squaring a number.
Here are two versions

``` python
def square_p(x):
    y = x*x
    print(y)

def square_r(x):
    y = x*x
    return y
```
If we then call square1=_p or square_r in the terminal, they both caculate the square and print it
``` python
>>> square_p(35)
1225
>>> square_r(35)
1225
```
but we treat these as mathematical functions and try to get their values, we see the difference.
For example, if we wanted to calculate 3*3+4*4 using our square function, it works with the 
``` python
>>> square_r(3)+square_r(4)
25
```
but doesn't work with the version which just prints the square and doesn't return it.
In this case it prints out 3*3 and 4*4 but returns a value called "None" and tries
to add those two "None"s together, which generates an error!
``` python
>>> square_p(3)+square_p(4)
9
16
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```

A function which doesn't have a return statement inside will always return a special value called "None"
and that value is generally not very useful!
