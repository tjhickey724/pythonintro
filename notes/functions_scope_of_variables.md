
## Scope of variables in functions
Scope refers to the places in a program that the values of a particular variable can be accessed and/or changed.

Code which is running in the body of a function has access to variables in 3 different scopes:
### built-in scope
These are the variables that are defined by Python such as print and input you can access them with dir(__builtins__).
Try this code
``` python
for x in dir(__builtins__):
    print(x)
```

### local scope
These are the variables defined in the function, including the parameters and any other variables that appear in the body
For example
``` python
def box_volumn(width, height, depth):
    vol = width*height*depth
    return vol
```
The local variables of box_volume are ```width, height, depth``` and ```vol```
The only code which can access these variables is the code inside that function...

### global scope
These are the variables whose values are defined outside of any function
For example
``` python
debugging = True

def square(x):
    if debugging:
        print(f'inside square function with parameter x={x}')
    s = x*x
    if debugging:
        print(f'square returns the value s={s}')
    return s
```
In the function above, if debugging is True then ```square``` will print info about the function begin called and returning;
otherwise it will just return thd square.

## Scope rules
The simple rules are that 
* all variables defined in the global frame (i.e. outside of any functions) can be accessed anywhere in the program, including inside function bodies,
* none of the global variables can be modified from inside a function (unless there is a global declaration in the function)
* local variables are only visible in the function where they are defined
* builtin variables are visible everywhere unless a global or local variale of the same name is in the scope.


## Global variables can be viewed from anywhere in a program
## but don't use global variables to pass data to functions!!!
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
This will raise an error because the variable d in the body is not defined anywhere.

``` python
import math
def degToRadian():  # the parameter was accidentally omitted
    r = d/180*math.pi
    return r
degrees = float(input("The degree is: "))
radians = degToRadian()
print('The degrees converted to radians is', radians)
```


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

The following code counts the number of times the square function is called
by using a global variable "counter" that gets modified inside the square function.

``` python
counter = 0

def square(x):
    global counter
    counter = counter + 1
    return x*x

print(counter)
for x in range(5,100,10):
    print(square(x))
print(f'counter={counter}')
```
