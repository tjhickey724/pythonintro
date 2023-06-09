# Variable Naming
The NAME can be any sequene of letters, digits, and underscores,
starting with a lowercase letter, EXCEPT that you can't use any of
the python keywords (e.g. def) and you shouldn't use any of the python
built-in function names (e.g. print) as you won't be able to use those
functions anymore as your function will "override" it.

If a variable contains multiple words, they are usually separated by underscores,
e.g. here are some valid python variables
``` python
say_hello
greeting
nth_fibonacci
calculate_amortization
```

### Python Keywords
Here is a list of they Python keywords which cannot be used as variable names, Python will object!
``` text
Keyword	Description
and	A logical operator
as	To create an alias
assert	For debugging
break	To break out of a loop
class	To define a class
continue	To continue to the next iteration of a loop
def	To define a function
del	To delete an object
elif	Used in conditional statements, same as else if
else	Used in conditional statements
except	Used with exceptions, what to do when an exception occurs
False	Boolean value, result of comparison operations
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
for	To create a for loop
from	To import specific parts of a module
global	To declare a global variable
if	To make a conditional statement
import	To import a module
in	To check if a value is present in a list, tuple, etc.
is	To test if two variables are equal
lambda	To create an anonymous function
None	Represents a null value
nonlocal	To declare a non-local variable
not	A logical operator
or	A logical operator
pass	A null statement, a statement that will do nothing
raise	To raise an exception
return	To exit a function and return a value
True	Boolean value, result of comparison operations
try	To make a try...except statement
while	To create a while loop
with	Used to simplify exception handling
yield	To end a function, returns a generator
```
don't worry about thier meanings, just try to avoid them.
Python will generate an error if you forget and try to use
one as the name of a function. You will learn how to use
all of these keywords by the end of the class.

### Built-in Python variables
Also, you should try to avoid using the built-in functions (like print) as variable names.
Here is a list of the current built-in python functions. 

Using one of these builtins
for the name of your own function won't cause an error, but you won't be able
to use that built-in function anymore as you will have redefined it!
``` text
abs, all, any, ascii, bin, bool, breakpoint, bytearray, bytes, 
callable, chr, classmethod, compile, complex, copyright, credits, 
delattr, dict, dir, divmod, enumerate, eval, exec, exit, 
filter, float, format, frozenset, getattr, globals, hasattr, hash, help, hex, 
id, input, int, isinstance, issubclass, iter, len, license, list, locals, 
map, max, memoryview, min, next, object, oct, open, ord, 
pow, print, property, quit, range, repr, reversed, round, 
set, setattr, slice, sorted, staticmethod, str, sum, super, 
tuple, type, vars, zip
```

### Online documentation
You can learn about any python value using the dir() or help() functions.
For example, the help function gives you information about any function (built-in or user-defined)
``` python
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```
and the dir() function shows the currently accessible variables, e.g.
if we define the say_hello function, then it will appear in the output of the dir() command
``` python
>>> def say_hello():
...     print('hello world')
... 
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__','say_hello']
>>> 
```
