# Files
Python allow you to read a string from a file using the open function
``` python
file = open(FILENAME,'r')  # the 'r' is to specify we will be reading from the file
data = file.read()  # this returns the file contant as one long string
file.close() # closes the file so it can be opened again later and reread if needed
lines = data.split('\n') # this returns a list of strings, one for each line
words = data.split() # this returns a list of all words 
```

The FILENAME needs to be a relative path or an absolute path to the file.

Relative means from where you opened vscode.

Absolute means from the root of your computer...

``` python
file = open(FILENAME,'w')
file.write(data)  # write the data to the file (but without a \n, add one if you need it
....
file.close()  # closes the file so it can be used by other programs
```

## Examples
Read a list of words
``` python
file = open('words5.txt','r')
words5 = file.read().split()
file.close()
```
Read 10K most common English words
``` python
file = open('words10K.txt','r')
words10K = file.read().split()
file.close()
```




