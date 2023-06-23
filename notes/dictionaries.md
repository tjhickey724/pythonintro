# Dictionaries
Dictionaries in Python are like lists except they are indexed by strings (or really any hashable value that could be in a set).

You can create a dictionary using the following notation
```
{key1:val1,  key2:val2,  .... , keyn:valn}
```
where the ```key```s are hashable types (strings, numbers, tuples of numbers, etc.)
and the ```val```s can be any Python value

For example,
```
person1 = {'name':'Tim', 'aga':67, 'gender':'male'}
person2 = {'name':'Caitlin', 'aga':28, 'gender':'female'}
course = {'name':'Intro to Python', 'enrolled':34, 'semester':'Sum23', 'coursenum':'COSI 10a', 'section':1}
```
We can access and modify the values in a dictionary using the ```d[k]``` indexing notation, which is similar to
indexing with lists and tuples, but the index for dictionaries is typically a string rather than an integer.
```
> print(person1['name'],person2['name'])
Tim Caitlin
> print(course['coursenum'],course['name'],' is offered in',course['semester'],'and enrolled',course['enrolled'])
COSI 10a Intro to Python was offered in Sum23 and enrolled 34
> person1['age'] += 1
> print(person1)
{'name':'Tim', 'aga':68, 'gender':'male'}
```

