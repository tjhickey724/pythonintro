# Python Classes

Python classes are created used the ```class``` keyword with the syntax
``` python
class CLASSNAME():
    class methods and class variables
```
The standard form of a class has special methods
* ```__init__(self,...)```  to initialize the object
*  ```__str__(self)```  to return a nice string representation of the object for printing
*  ```__eq__(self, other)```  to test if the object is equal to another object

Other methods are defined like functions but the first parameter is always ```self```
Here is an example of the class representing Complex numbers
``` python
class Complex():
    def __init__(self,a,b):
        self.re = a
        self.im = b
    def __str__(self):
        return f'{self.re}+{self.im}i'
    def __eq__(self,other):
        return self.re==other.re and self.im==other.im
    def add(self,other):
        return Complex(self.re+other.re, self.im+other.im)
    def mul(self,other):
        return Complex(self.re*other.re - self.im*other.im, self.re*other.im+self.im*other.re)
    
    def __add__(self,other):
        ''' allow user to write x+y for x.add(y) '''
        return self.add(other)
    def __mul__(self,other):
        ''' overloading: allow user to x*y for x.mul(y)'''
        return self.mul(other)
```
and we can use it like this
``` python
z = Complex(1,1)
w = Complex(1,2)
u = z.mul(w)
v = z*w
print(z,w,u,v,u==v)
```
## Exercise
Add the methods ```sub, div, __sub__, __truediv__``` to the Complex class and show how to use them
(note that ```__truediv__``` is the operator for handling "x/y" not ```__div__```


## Objects versus Dictionaries
Both a dictionaries d and an object x allow us to store values in a python value and access it by name but
* dictionary values are accessed with indexing:  ```d['re']```
* python object values are accessed with the dot notation:  ```x.re```

Python methods are like functions except they are called using dot notation,e.g.
* ```len("abc")```  is an example of calling the ```len``` function on the string object ```abc```
* ```"abc".upper()``` is an example of calling the ```upper``` method on the string
* ```"hello,there,world".split(',')``` is an example of calling the split mmethod on the string using a parameter ','

  
