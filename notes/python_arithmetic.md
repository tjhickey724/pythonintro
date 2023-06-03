# Python Arithmetic
Python allows you to work with four kinds of numbers
* integers like 5, 2023, -100, 0
* decimal numbers like 3.1415, 10.99, -2.718281828
* complex numbers like 1+2j   (where j is the imaginary number in Python)
* fractions: like 1/2 and 355/113

We will only look at the first two types. You can read about complex numbers and fractions on your own if interested.

## Operations
Python can be used like a calculator with the standard arithmetic operaitons, +,-,*,/
*  addition 5+2
*  subtraction 5-2
*  multiplication 5*2
*  division  5/2

But it has some additional operators
* integer division 15//2  (which throws a way the remainder, so 15//2 = 7 as 15=2*7 + 1)
* integer remainder 15%2  (which returns the remainder, fo 15%2 = 1 as 15 = 2*7+1)
* raising to a power 15**2  (which returns 225)


You can consult the official documentation to see all of the [Python numeric operators](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

## Math package
You can also get access to a large set of Mathemtical functions (sin, cos, exp, log, etc.)
by importing the math package. Here are all of the function you can access
``` python
acos acosh asin asinh atan atan2 atanh 
ceil comb copysign cos cosh degrees dist 
e erf erfc exp expm1 fabs factorial floor 
fmod frexp fsum gamma gcd hypot inf 
isclose isfinite isinf isnan isqrt 
lcm ldexp lgamma log log10 log1p log2 modf nan 
nextafter perm pi pow prod radians remainder 
sin sinh sqrt tan tanh tau trunc ulp
```
but you need to preface them with "math", e.g.
``` python
import math
help(math) # this prints documentation about all of the math functions
print(math.cos(math.pi/2))  # this prints cos(pi/2)
print(math.log10(2023))  # this prints the log base 10 of 2023
```
