# Files
Python allow you to read a string from a file using the open function
``` python
file = open(FILENAME,'r')  # the 'r' is to specify we will be reading from the file
data = file.read()  # this returns the file contant as one long string
lines = data.split('\n') # this returns a list of strings, one for each line
words = data.split() # this returns a list of all words 
```

The FILENAME needs to be a relative path or an absolute path to the file.

Relative means from where you opened vscode.

Absolute means from the root of your computer...

