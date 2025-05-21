# LP1 - Amortization Calculator
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

# What to hand in.
Create two short narrated Zoom movies (less than 60 seconds)
1. where you show yourself running the program on these two inputs in VScode
2. where you show yourself explaining what your program is doing and why it is correct. Don't read the program, explain it as if you were talking to another programmeer on your team

Cut and paste your code into the LP1 textbox in the Mastery Learning App and add a comment at the top with your name, email, and links to your two movies.

Note - you should not use any loops or conditionals for this program just use input, print, float, and arithmetic.
      
