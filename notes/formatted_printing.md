# Formatted Printing
When we use Python to print out a table of numbers, we like the values to line up neatly in columns.
Python has many ways to do that. Here we show one approach using the % operator.

The general form is
``` python
print(FORMAT_STRING%(v1,v2,...,vn))
```
where the v1,v2, ..., vn are expressions that produce values (typically numbers or strings)
and the Format string has a syntax for specifying how each of those values should be printed.
For example,
``` python
print("a=%3d, b=%3d, a/b=%10.5f - %5s"%(355, 113, 355/113, 'bye'))
```
This will print
``` text
a=355, b=113, a/b=   3.14159 -   bye
```
Here the FORMAT_STRING is
``` python
"a=%3d, b=%3d, a/b=%10.5f - %5s"
```
where
* %3d means to print an integer using at least 3 spaces
* %10.5f means to print a float using at least 10 spaces with exactly 5 spaces after the decimal point.
* %5s means to print a string value using at least 5 spaces




We can also have the answer left justified (using a %-10.5f), e.g.
``` python
print("a=%3d, b=%3d, a/b=%-10.5f - %-5s"%(355, 113, 355/113, 'bye'))
```
This will print
``` text
a=355, b=113, a/b=3.14159    - bye
```
