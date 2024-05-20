# Printing Strings

The simplest Python program is one that prints a greeting
``` python
print('Hello World!')
```

As always, you should cut/paste the code examples into a Python interpreter (e.g. Visual Studio Code or pythontutor.com)
to make sure you understand the syntax and semantics of this program feature.

The print statement causes the Python interpreter to display some characters on the output terminal.
Try running this program in Visual Studio Code.
Or visit [Python Tutor](https://pythontutor.com) and run it there.

## Strings
The syntax for a simple print statement is
``` python
print(STRING)
```
where STRING is a quoted sequence of characters, e.g.
``` python
print('this string has single quotes')

print("this string uses the double quote")

print(''' this string uses triple quotes,
and it can continue over
multiple lines, but singly quoted strings can not!''')

print(""" this string uses triple double quotes
and it also extends over multiple lines""")
```

So, you can create a string using 4 different kinds of quotes...
single apostrophes ('), single quotation marks ("), or triple apostroples ('''),
or triple quotation marks (""")

## Printing special characters
If your string uses single apostrophe's and you want to include an apostrophe 
in your string, you need to "escape" it by putting a backslash (\) in front of it, e.g.

``` python
print('This quote\'s interesting as it contains an apostrophe (\') as you can see')
```

If we didn't add the backslash then Python would think the string ended when it saw the apostrophe.
You can include an apostrophe in a string which uses quotation marks, without escape it though.

``` python
print("This quote's interesting as it contqains an apostrophe(') as you can see")

print("This quote contains both apostrophes (') and quotation marks (\") so it needs to use an escape")

print('''Triple quotes allow you to use apostrophes (') and quotation marks (") without escaping them!''')
```

The backslash notation is also used to introduce other characters into a string [more details](https://python-reference.readthedocs.io/en/latest/docs/str/escapes.html)
For example, \n add a new line character, \t adds a tab, \\ adds a backslash

Also, Python strings can contain characters from any of the standard [Unicode characters](http://www.unicode.org/charts/)

For example,
``` python
print('山')
``` 
will print the Japanese character yama for Mountain, if you have that character set intalled on your computer.



