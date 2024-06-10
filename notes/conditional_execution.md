# Conditional Execution

In Python, we use the if/elif/else statement to write a program which executes different code based on the input.

## Syntax
The basic if statement has the form
``` python
if TEST:
    STATEMENTS
```
it will evaluate the TEST which is considered a Boolean expression (i.e. returns a truthy or falsy value).
If the result is one of the following it is considered to be False
* False, 
* None, 
* 0 or 0.0 
* ""
* empty containers (lists, dicts, tuples, etc, which we will see later)

Otherwise it is considered to be true.

## Comparisons
The typical way to get a boolean value is by comparing numbers with one of the standard operators
* x<y  less than
* x>y  greater than
* x<=y less than or equal
* x>=y  greater than or equal
* x==y  equal
* x!=y  not equal

Python also allows multicomparisons
* 2 < x <= 10
* 100 >= x > 93
  
We can also combine the relations with boolean operators
* E and F   both E and F are true
* E or F    either E or F or both are true
* not E     E is false

For example
* (1<x) and (x < 100)
* (x<5) or (x==10)

and these can be combined using paraentheses or boolean PEMDAS, where ```not``` binds tightest, then ```and``` then ```or``

## Membership
We can test for membership 
* x in [1,3,5,7]
* y in {5,6,7}
* vowel in "aeiou"
  
## if/else
We can also specify two outcomes depending on the result of the test with the if/else statement
``` python
if TEST:
    THEN_STATEMENTS
else:
    ELSE_STATEMENTS
```

``` python
percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")
else:
    if percent >= 80:
      print("You got a B!")
    else:
        if percent >= 70:
            print("You got a C!")
        else:
            if percent >= 60:
                print("You got a D!")
            else:
                print("You got an F!")
print('bye')
```

## Nested if/elif/else
Finally, if there are multiple tests we can use the if/elif/else statement
to try each one in turn until we find one that evaluates to true, in which case the rest are skipped

``` python
if TEST1:
   STATEMENTS1
elif TEST2:
   STATEMENTS2
...
else:
   ELSE_STATEMENTS
```
  where the last ```else``` clause can be omitted.
  
``` python
percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")
elif percent >= 80:
    print("You got a B!")
elif percent >= 70:
    print("You got a C!")
elif percent >= 60:
    print("You got a D!")
else:
    print("You got an F!")

print('bye')
```
  

