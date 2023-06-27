# Reading Excel files
Python is frequently used to analyze data and one of the most common forms of such data is excel files exported in the
comma separated values format (csv)

Python has a package, csv,  that lets you easily read a CSV file into a list of dictionaries,

## Reading a CSV file
For example to read the data from a CSV file 'courses.csv'
we can use the following code. This takes the first line of the
file as the keys of the dictionary.
``` python
import csv
with open('courses.csv') as csvfile:
    data = list(csv.DictReader(csvfile,delimiter=','))
print(len(data))
```
