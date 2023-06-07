# Default Parameters

Python allows you to define functions with default parameters which are optional.
We have seen this with the "end" parameter of the print function.
``` python
for i in range(4):
    print(i)
print('done')
```
will print its argument, 0, and then print a newline character `\n` and the print 1 and a newline, etc.
``` text
0
1
2
3
done
```
If you would rather it not print the newline, but print a comma and a space instead you can type
``` python
for i in range(4):
    print(i,end=", ")
print('done')
```
which results in
``` text
0, 1, 2, 3, done
```
The "end" parameter is optional and has default value '\n'

## defining functions with default parameters
You can add default parameters to your own functions,
for example,
``` python
def scale(val,max_val=100):
    return val/max_val
print('40/100 = ',scale(40))
print('40/50  =', scale(40,max=50))
```
This will print
``` text
40/100 = 0.4
40/50  = 0.8
```
You need to add any default parameters after the usual parameters...
The following example shows a function which will return the proportional
distance a value is between the min_val and max_val with the defaults being
0 and 100. Notice that we can omit the parameter name, if it is in the right
position, but otherwise we need to use it.

``` python
def scale(val,min_val=0,max_val=100):
    return (val-min_val)/(max_val-min_val)
print(scale(40))
print(scale(40,max_val=50))
print(scale(40,20,60))
print(scale(40,20))
```

