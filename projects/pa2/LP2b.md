# LP2b - Descriptive Statistics

This assignments tests your ability to use lists and loops.

Your program should prompt the user to enter a list of integers.
It should first ask them to enter the size N of the list,
and then prompt them for each of the numbers.

Once it reads the list it should print the list out in sorted order
and then calculate the following values and print them out:
1. the sum
2. the largest and smallest values (max and min)
3. the mean (the sum divided by N)
4. the median (i.e. the middle value if the array is sorted)
5. the mode (which value appears most often, if there are multiple, then the largest one)
6. the variance (the sum of (x-mean)^2/N  over all x in the list
7. the standard deviation (sqrt of the variance)

You should not import any package for this and write this as one big script,
don't define any functions or modules. You can use the Python builtin functions
for len, sum, max, and min.

Here is a sample run, your output should be identical to this:
```
Enter N: 4
Enter the 4 elements of the list
1> 5
2> 2
3> 5
4> 2
5> 4
The sorted list is 2 2 4 5 5
sum is 18
max value is 5
min value is 2
mean is 3.6
median is 4
mode is 5
variance is 2
standard deviation is 1.414
```

# What to hand in
Hand in the code with a comment at the top containing your name and email and links to two short movies (< 2 minutes)
1. A movie showing you running this program in VScode with the inputs shown as above
2. A movie showing you running the program in Python tutor explaining what the program does to the memory and why that is giving the correct answers.

Submit this on the Mastery Learnig App.
