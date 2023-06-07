# Functions returning useful values

Functions in Python are expressions that always return a value. 
If the function body doesn't explicitly contain a return statement,
then the return value is the special Python value ``` none```

To return a value from a function, you use the return statement
``` python
    return(EXPRESSION)    # the parentheses are optional for return statements
```
which will
* evaluate the EXPRESSION to get a Python value,
* stop evaluating any more statements in the body of the function, and
* return the value to the parent frame

For example, the following program finds the volume and surface area of a cylinder
``` python
import math
def cylinder_volume(radius, height):
    base_area = math.pi*radius**2
    volume = base_area*height
    return(volume)

def cylinder_surface_area(radius, height):
    base_area = math.pi * radius**2
    base_circumference = 2*math.pi * radius
    side_area = base_circumference * height
    return 2*base_area + side_area

def calc_cylinder_stats():
    print("Cylinder Calculator")
    r = float(input("radius: "))
    h = float(input("height: "))
    volume = cylinder_volume(r,h)
    area = cylinder_surface_area(r,h)
    print(f'The volume of a cylinder of radius {r} and height {h} is {volume}')
    print(f'and the surface area is {area})

calc_cylinder_stats()
 
```

## Global Variables and functions

``` python
import math
def degToRadian():
    global r
    r = d/180*math.pi
    #return r
d = float(input("The degree is: "))
r = 0
degToRadian()
print (r)
```
Better to run it this way:
``` python
import math
def degToRadian(d):
    r = d/180*math.pi
    return r
d = float(input("The degree is: "))
degToRadian(d)
print (r)
```
