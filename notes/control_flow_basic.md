# Control Flow Basic

Python programs typically consist of a collection of function definitions
together with a single function call (typically called main).

Here is a simple example of a Python program.
``` python
def say_hello():
    print("Hello World!")

def say_hello2():
    say_hello()
    say_hello()
    say_hello()
    say_hello()

def say_hello3():
    say_hello2()
    say_hello2()
    say_hello2()
    say_hello2()

def main():
    say_hello3()
    
main()
```
Calling '''say_hello()''' will print '''Hello World!'''  once.

Calling '''say_hello2()''' will call '''say_hello()''' four times and so print '''Hello World!'''  four times.

Calling '''say_hello3()''' will call '''say_hello2()''' four times, and each time will print 4 '''Hello World!'''s

So running this program, will print "Hello World!" sixteen times.

Do you see why? What if we defined a say_hello4() in a similar
fashion. How may Hello's would that print? or a say_hello5()?? or say_hello6()??

Visit the [pythontutor.com](https://pythontutor.com) site, cut/paste the program, and step through its evaluation.
Notice that Python keeps track of where it is in the program by using a "Stack" of function names. Each time it calls a function
it pushes that function name (and its location in the function) on to the Stack, when it returns from the function it pops the function
name (and location) off of the stack. this allows it to keep track of where it is in the program....

