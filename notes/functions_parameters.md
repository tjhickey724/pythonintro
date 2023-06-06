# Functions with Parameters
Python allows you to pass values into parameters. That value then becomes
a local variable for the statements in the function. When all of the statements 
have been evaluated the variable disappears.

The syntax for defining a function with parameters is to add the parameters names,
separated by commas to the definition line:
``` python
def NAME(V1,V2, ..., Vn):
    STATEMENTS
```
You can a function with parameters with the following syntax:
``` python
NAME(E1, E2, ..., En)
```
where '''E1,...,En''' are Python expressions

## Examples

``` python
'''
This is a song for people with a lot of time on their hands!
'''

def print_verse(n):
   print(n,'bottles of beer on the wall')
   print(n,'bottles of beer')
   print('Take one down, pass it around')
   print(n-1,'bottles of beer on the wall')
   print()
def print_song(k):
    print(k,'Bottles of Beer Song')
    print()
    for i in range(k,0,-1):
        print_verse(i)

print_song(100)

```

and here is an example of a program to print form letters with
three parameters: name, date, and hour
``` python
def print_form_letter(name,date,hour):
    print('Dear',name+',')
    print()
    print('Congratulations you have been invited to a job interview on',date,'at',hour,'pm')
    print('Hope to see you there!')
    print()
    print('Sincerely,')
    print('The Management')
    print('-'*40)

hour = 1
print_form_letter('Nan Wang','7/1/23',hour)
print_form_letter('Zheng Zheng','7/1/23',hour+1)
print_form_letter('Karen Mai','7/1/23',hour+2)
```
