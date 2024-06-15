
## Scope of variables in functions
Scope refers to the places in a program that the values of a particular variable can be accessed and/or changed.

The simple rules are that 
* all variables defined in the global frame (i.e. outside of any functions) can be accessed anywhere in the program, including inside function bodies,
* none of the global variables can be modified from inside a function (unless there is a global declaration in the function)

## Global variables can be viewed from anywhere in a program
Here is an example of a typical Python function to convert degrees to radians:
``` python
import math
def degToRadian(d):
    r = d/180*math.pi
    return r
degrees = float(input("The degree is: "))
radians = degToRadian(degrees)
print('The degrees converted to radians is', radians)
```
One common mistake is to omit the parameter (d) 
and in this case, the program would still produce the right answer
as the "d" in the body of the function would refer to the global variable "d"
``` python
import math
def degToRadian():  # the parameter was accidentally omitted
    r = d/180*math.pi
    return r
degrees = float(input("The degree is: "))
radians = degToRadian()
print('The degrees converted to radians is', radians)
```
This will raise an error because the variable d in the body is not defined anywhere.

A slight modification of the program would work however, if the global variable was called "d" and not "degrees"
``` python
import math
def degToRadian():  # the parameter was accidentally omitted
    r = d/180*math.pi
    return r
d = float(input("The degree is: "))
radians = degToRadian()
print('The degrees converted to radians is', radians)
```
What happens here is that the variable "d" in the function body, isn't a parameter of the function and isn't defined in the function, so Python looks for it in the Global Variable list, and it finds it!  The global variables are all visible and accessible inside the body, so this wil actually return the correct result in this case.

Why might this be a bad idea?  

What are the benefits of passing values in parameters instead of with global variables?

## Function variables can not be viewed outside of their bodies
Suppose we replaced the return(r) with a print(r), what would happen?

``` python
import math
def degToRadian(d):
    r = d/180*math.pi
    print(r)
degrees = float(input("The degree is: "))
radians = degToRadian(degrees)
print('The degrees converted to radians is', radians)
```
When you run this it will print out the right answer on a line by itself then it will print:
``` text
The degrees converted to radians is None
```
because the ```degToRadian``` function has not return statement and so will return the Python value ```None```

Suppose we changed the function variable from ```r``` to ```radians``` as in the global variable, 
would that work?

``` python
import math
def degToRadian(d):
    radians = d/180*math.pi
degrees = float(input("The degree is: "))
radians = 0
degToRadian(degrees)
print('The degrees converted to radians is', radians)
```

No, this won't work.
When degToRadian(degrees) is called, Python will create a new stack frame with
a new variable ```radians``` and changing that variable in the stack frame will
not effect the global variable ```radians```

If we really wanted it to work, we could declare that radians is a global variable
and shouldn't be created in the stack frame, this would work but is seen as bad practice.

``` python
import math
def degToRadian(d):
    global radians
    radians = d/180*math.pi
degrees = float(input("The degree is: "))
radians = 0
degToRadian(degrees)
print('The degrees converted to radians is', radians)
```

What are the disadvantages of using Global Variables like this?

Why would it be better to use the return function?

## Modifying Global variables inside a function
If you want to modify a global variable from inside a function you must 
declare the variable to be "global" in the body of the function.
This is generally not a good practice, but we include it here so if you see it
in the future you'll understand the code.

``` python
square_counter = 0

def square(x):
    global counter
    counter = counter + 1
    return x*x

print(counter)
for x in range(5,100,10):
    print(square(x))
print(f'counter={counter}')
```
