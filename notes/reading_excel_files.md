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
with open('people.csv') as csvfile:
    data = list(csv.DictReader(csvfile,delimiter=','))
print(len(data))
```

## Write a list of dictionaries to a CSV file
First we create a list of dictinoaries:
``` python
people = [
 {'name': 'Tim', 'age': 67, 'height': 68},
 {'name': 'Ryan', 'age': 24, 'height': 68},
 {'name': 'Caitlin', 'age': 28, 'height': 64},
 {'name': 'David', 'age': 19, 'height': 59},
 {'name': 'Toby', 'age': 18, 'height': 59},
 {'name': 'Anna', 'age': 18, 'height': 57},
 {'name': 'Jason', 'age': 20, 'height': 68},
 {'name': 'Jennifer', 'age': 20, 'height': 64},
 {'name': 'Penny', 'age': 22, 'height': 64},
 {'name': 'Sara', 'age': 33, 'height': 65},
 {'name': 'Greg', 'age': 45, 'height': 72},
 {'name': 'Julian', 'age': 17, 'height': 67},
 {'name': 'Lebron', 'age': 38, 'height': 81},
 {'name': 'Jayson', 'age': 25, 'height': 80},
 {'name': 'Novak', 'age': 36, 'height': 74},
 {'name': 'Mike', 'age': 42, 'height': 72},
 {'name': 'Kayla', 'age': 16, 'height': 62},
 {'name': 'Kendrick', 'age': 29, 'height': 76},
 {'name': 'Aria', 'age': 20, 'height': 68},
 {'name': 'Emma', 'age': 18, 'height': 65},
 {'name': 'Sophia', 'age': 60, 'height': 80},
 {'name': 'John', 'age': 54, 'height': 91},
 {'name': 'Joe The Giraffe', 'age': 23, 'height': 334},
 {'name': 'Bob', 'age': 21, 'height': 67},
 {'name': 'Louis', 'age': 31, 'height': 67},
 {'name': 'Luci', 'age': 90, 'height': 80},
 {'name': 'Ruth', 'age': 66, 'height': 54},
 {'name': 'Josh', 'age': 29, 'height': 87},
 {'name': 'Helen', 'age': 29, 'height': 84},
 {'name': 'Sarah', 'age': 20, 'height': 3},
 {'name': 'Jomothy', 'age': 29, 'height': 59},
 {'name': 'Piter', 'age': 54, 'height': 70},
 {'name': 'Limmy', 'age': 9, 'height': 53},
 {'name': 'Sam', 'age': 20, 'height': 65},
 {'name': 'Cass', 'age': 21, 'height': 66},
 {'name': 'Jim', 'age': 19, 'height': 72}]
```
Then we can write it to a file using the following
``` python
import csv
f = open('people.csv','w')
z = csv.DictWriter(f,list(people[0]))
z.writeheader()
z.writerows(people)
f.close()
```
