
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
