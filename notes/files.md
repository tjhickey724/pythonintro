# Files
Python allow you to read a string from a file using the open function
``` python
file = open(FILENAME,'r')
data = file.read()  # this returns the file contant as one long string
lines = data.split('\n') # this returns a list of strings, one for each line
words = data.split() # this returns a list of all words 
```

