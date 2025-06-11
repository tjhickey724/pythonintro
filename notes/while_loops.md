## while loops

The syntax of a while loop is
``` python
while TEST:
    STATEMENTS
```

A while loop is evaluated by first evaluating the TEST
if it evaluates to True, then the STATEMENTS are evaluated
and it repeats the process by evaluating the TEST again, etc.

if the TEST evaluates to a False value, then it skips the
statements and the while loops is complete.

## while loops to read in a list of values with a sentinel
A common use of while loops is to prompt the user for a sequence
of input ending with some particular value and to store the values
in a list or do some other computation on those values. Here is
an example

``` python
values = []
print('enter positive numbers ending with a zero')
value = int(input("> "))
while value>0:
    values = values + [value]
    value = int(input("> "))
print('you entered',values)
print('here is the sorted list of unique values',sorted(set(values)))
```

### the ```break``` statement
Inside a loop, one can use the ```break``` statement to end the loop.
In general though it is better to use the TEST to end the loop rather
than including a break statement
e.g.
``` python
print('Calcuate square roots and enter zero to quit')
while True:
    x = float(input("Enter a positive number: "))
    if x<=0:
        print("you were supposed to enter positive numbers!!")
        break;
    print('the square root of x is',x**0.5)
```
We can avoid the break statement by rewriting the loop as follows:
``` python
print('Calcuate square roots and enter zero to quit')
x = float(input("Enter a positive number: "))

while x> 0:
    print('the square root of x is',x**0.5)
    x = float(input("Enter a positive number: "))
print("you were supposed to enter positive numbers!!")

print('done')
```


### the ```continue``` statement
The ```continue``` statement appearing in a loop, causes Python to skip the
rest of the statements in the loop and to jump back to the TEST.
Here is an example,
``` python
print('Calcuate square roots and enter zero to quit')
while True:
    x = float(input("Enter a positive number: "))
    if x<0:
        print("you were supposed to enter positive numbers!!")
        continue;
    elif x==0:
        break
    print('the square root of x is',x**0.5)
```

We can rewrite this without continue or break as follows:
``` python
print('Calcuate square roots and enter zero to quit')
x = float(input("Enter a positive number: "))
while x != 0:
    if x<0:
        print("you were supposed to enter positive numbers!!")
    else:
        print('the square root of x is',x**0.5)
    x = float(input("Enter a positive number: "))
print("Done!")
```

How does this differ from the previous program?

## Infinite loops
If you are not careful, the while loop might never stop, e.g.
```
x=1
while (x>0):
  x=x+1
  print(x)
```
If this happens you need to use CTRL-C to kill the job.

## Examples

### Guessing Game
Let's implement this game:
* generate a random integer in the range 0 1000
* store it in the variable ```answer```
* ask the user to make a guess
* if they guess the answer end the loop
* if not, tell them if it is too big or too small
* count the number of guesses they make

### Robot Psychologist
Try this one
have a conversation with the user and pick a random response to each of their comments.
Stop when they say "goodbye"

### Hangman
* pick a random word from a list
* ask the user to try to guess letters
* keep track of wrong guesses
* stop when wrong guesses is 7 or more, or when they've guessed all the letters
* print out a clue after each guess (showing the letters they got right and a dash for missing letters)

### Wordle
* pick a random 5 letter word from a list
* ask the user to guess a 5 letter word
* print out a clue showing which letters are in correct position, which are in word, and a dash for letters not in word.



