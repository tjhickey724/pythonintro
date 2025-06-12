# Basic Function Syntax and Semantics in Python

We can define a function in Python using the "def" keyword.

A function is a named collections of Python statements that can be evaluated
when the function is called.

For example, here is the way to define a function print two lines "Hello World" and "How are you today?"
and after that we call the function three times:
``` python
def say_hello():
    print("Hello World!")
    print("How are you, today?")
    print()
say_hello()
say_hello()
say_hello()
```
which will result in the following output:
``` text
Hello World!
How are you, today?

Hello World!
How are you, today?

Hello World!
How are you, today?

```
## Defining a function with no parameters
In general, the syntax for defining this simple form of a function is
``` python
def NAME():
    statement1
    statement2
    ...
    statementn
```
where the first line has 
* the keyword "def" 
* followed by a space
* followed by the NAME of the function you are defining
* followed by parentheses ()
* followed by a colon
* followed by the statements that make up the body of the function
which are all indented the same amount (usually with a tab or 4 spaces)

For now, the statements are either print statements
or function calls!

## Calling a function with no parameters
and the syntax for calling such a function is
``` python
NAME()
```

## Print Menu
A good application of no-parameter print functions
is to print a menu of choice for the user to take...





