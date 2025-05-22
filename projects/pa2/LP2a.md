# LP2a: Heron's Formula with Error Checking

This assignment tests your ability to use if/elif/else conditional statements.

Write a Python script to find the area of a triangle with sides of length a,b,c using Heron's formula,
you can look it up online, but add error checking... 
The script should ask the user to enter numbers a, b, c and should run the following checks:
* if a,b,or c is negative then tell the user they must be positive
* if a+b<c, tell the user that side c is too long
* if a+c<b or b+c<a tell the user that side c is too short
* otherwise calculate the area and print it.

Here are some examples of running the script multiple times.
Your script should produce exactly the same output!
```

============= RESTART ============
Triangle Area Script
Enter the lengths, a,b,c of three sides of a triangle
a: 3
b: 4
c: -1
a, b, and c must be positive

============= RESTART: ============
Triangle Area Script
Enter the lengths, a,b,c of three sides of a triangle
a: 3
b: 4
c: 8
side c is too long

============= RESTART: ============
Triangle Area Script
Enter the lengths, a,b,c of three sides of a triangle
a: 2
b: 4
c: 1
side c is too short

============= RESTART: ============
Triangle Area Script
Enter the lengths, a,b,c of three sides of a triangle
a: 3
b: 4
c: 5
the area is 6.0
            
```

# What to hand in
Cut/paste your code into the Master Learning App for PL2 and add a comment at the top
with your name and email and links to two short movies (< 2 minutes) as described below:
1. A movie showing you running your program using VScode with the inputs shown above
2. A movie where you explain how your program works and why it correctly meets the requirements above

