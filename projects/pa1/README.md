# PA1
This PA tests your understanding of variables, expressions and pytbon programming enviornments.

* [LP1 - Amortization](LP1.md)
* [CP1 - Custom Calculator](CP1.md)


## LP1 - Amortization
Write a Python program which will compute the first four lines of an Amortization schedule.
It should ask the user for the initial balance 'b', interest rate 'r', and payment amount 'a'

The for each of the first four payments it calculates the new  balance b as follows:
* calculate the interest  i  = b*r
* subtract the interest from the payment to get the principle p paying down the balance p = a - i
* notice that the payment amount a is i+p
* subtract p from the balance to get the new principle b = b - p
print the interest i, principle p, and balance b   

Your program should produce *exactly* the following output for the two cases shown below ...
```
Amortization Schedule for 4 payments
Enter principle: 1000
Enter interest rate, e.g. 0.05 for 5%: 0.1
Enter payment: 300
 n   interest  principle    balance
 1     100.00     200.00     800.00
 2      80.00     220.00     580.00
 3      58.00     242.00     338.00
 4      33.80     266.20      71.80


Amortization Schedule for 4 payments
Enter principle: 1000
Enter interest rate, e.g. 0.05 for 5%: 0
Enter payment: 250
 n   interest  principle    balance
 1       0.00     250.00     750.00
 2       0.00     250.00     500.00
 3       0.00     250.00     250.00
 4       0.00     250.00       0.00
```

### What to hand in.
Create two short narrated Zoom movies (less than 60 seconds)
1. where you show yourself running the program on these two inputs in VScode
2. where you show yourself explaining what your program is doing and why it is correct. Don't read the program, explain it as if you were talking to another programmeer on your team

Cut and paste your code into the LP1 textbox in the Mastery Learning App and add a comment at the top with your name, email, and links to your two movies.

Note - you should not use any loops or conditionals for this program just use input, print, float, and arithmetic.
      

## CP1 - a Creative Programming assignment

Write a Python program which asks the user for their name
and prompts them for some numbers (integers and/or floats) 
and then does several calculations and prints out the answers nicely
with formatted printing (so fix the number of digits after the decimal point).

For example, you could write a program to convert dollars to different currencies.
Ask the user for the amount of dollars and then convert that into several different currencies

Or you could write a program to find the volumes of several different solids, 
e.g. find the volume of a sphere by asking for the radius,
then find the volume of a cylinder by asking for the radius and height,
then ....

Or you could write a program to calculate how much each person owes 
if they go out to dinner and split the bill equally for a given tax and tip rate.

Just pick something which demonstrates your ability to prompt the user for numbers, do calculations, 
and print the results out in a nicely formatted way.

Create 2 short narrated Zoom movies
1. Showing you running your program in VScode and explaining how to use it
2. Showing you explaining each line of your program and how it works.

Cut/paste your code into the PA1 textbox in the Mastery Learning App and add a comment at the top with links to the two movies.
            
