# Variables
Python allows you to store values in named locations in memories
and to use these valuation in various calculations (e.g. arithemtic).

Variable names are sequences of letters, digits, and underscores,
starting with a lowercase letter. There are [some additional restrictions as well](./variable_names.md)

You can store values in a variable using the = symbol.
You can also use variables in formulas and Python will look up the value stored in the variable, e.g.
``` python
a = 355
b = 113
print(a,b,a/b)
```

Formulas are evaulated using the usual PEMDAS rules.
You can see how Python stores values in variables using the [Python Tutor](https://pythontutor.com)

## Examples
``` python
# this converts 60 miles per hour into feet per second
miles_per_hour = 60
feet_per_second = miles_per_hour*5280/3600
print(feet_per_second)
```

``` python
# this finds the solutions to ax^2 + bx +c =0 using the quadratif formula
import math # we need this to take the square root with math.sqrt
a=1
b=5
c=6
d = b*b-4*a*c
x1 = (-b + math.sqrt(d))/(2*a)
x2 = (-b - math.sqrt(d))/(2*a)
print(a,b,c,x1,x2)
```

