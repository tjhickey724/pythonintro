# Dictionaries
Dictionaries in Python are like lists except they are indexed by strings (or really any hashable value that could be in a set).
Dictionaries are often used to represent complex data objects that have multiple features with multiple different types of values.

You can create a dictionary using the following notation
``` python
{key1:val1,  key2:val2,  .... , keyn:valn}
```
where the ```key```s are hashable types (strings, numbers, tuples of numbers, etc.)
and the ```val```s can be any Python value

For example,
``` python
person1 = {'name':'Tim', 'age':67, 'gender':'male'}
person2 = {'name':'Caitlin', 'age':28, 'gender':'female'}
course = {'name':'Intro to Python',
          'enrolled':30,
          'semester':'Sum25',
          'coursenum':'COSI 10a',
          'section':1}
```
We can access and modify the values in a dictionary using the ```d[k]``` indexing notation, which is similar to
indexing with lists and tuples, but the index for dictionaries is typically a string rather than an integer.
```
> print(person1['name'],person2['name'])
Tim Caitlin
> print(course['coursenum'],course['name'],' is offered in',course['semester'],'and enrolled',course['enrolled'])
COSI 10a Intro to Python was offered in Sum23 and enrolled 34
> print(f"{course['coursenum']} {course['name']} is offered in {course['semester']} and enrolled {course['enrolled']}")
COSI 10a Intro to Python was offered in Sum23 and enrolled 34
> person1['age'] += 1
> print(person1)
{'name':'Tim', 'aga':68, 'gender':'male'}
```

---

# Once we learn about loops

We can iterate through the keys of a dictionary using the usual for loop syntax
``` python
> for key in course:  print(key,' :: ',course[key])
name :: Intro to Python
enrolled :: 34
semester :: Sum23
coursenum :: COSI 10a
section :: 1
```

