# Lists
A Python list stores a sequence of any Python objects.

## Creating lists
They can be created using square brackets with the Python elements separated by commas, e.g.
``` python
> primes = [2,3,5,7,11,13,17,19]
> articles = ['a', 'an', 'the']
> misc = [0, 'hello', 3.14159, True, 2.718281828]
> poem = ['Two', 'roads', 'diverged', 'in', 'a', 'yellow', 'wood']
```

## Indexing and slicing
Lists can be indexed and sliced in the same way that strings are
``` python
> print(poem[2])
diverged
> print(poem[2:5])
['diverged','in','a']
> print(poem([-2]))
yellow
```

## concatenation
You can add concatenate two lists with "+" just as with strings
``` python
> x = [1,2,3] + [3,4,5]
> print(x)
[1,2,3,3,4,5]
```
and you can multiply lists which makes multiple copies
``` python
> print([1,2]*3)
[1.2,1,2,1,2]
```
You can add a single element to the end of a list in two ways
``` python
> x=[1,2,3]
> print(x)
[1,2,3]
> x = x+[4]
> print(x)
[1,2,3,4]
> x.append(5)
> print(x)
[1,2,3,4,5]
```
## List methods
Python has several useful built-in methods on lists:
``` python
 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
 ```
* ```L.append(Y)``` adds the element Y to the end of the list L
* ```L.clear()``` removes all elements from the list L
* ```L.copy()``` returns a copy of the list L
* ```L.count(Y)``` returns the number of times that element Y appears in list L
* ```L.index(Y)``` returns the index of the first occurrence element Y in the list L (and -1 if Y doesn't appear in L).
  * ```L.index(Y,start,end)``` returns the index of first occurrences of Y between the indices start and end in the list L
* ```L.insert(P,Y)``` inserts Y at position P in L
* ```L.pop()``` removes the last element from L
* ```L.reverse()``` reverses the elements in L
* ```L.sort()``` sorts the elements in L

## Splitting a string into a list of words or list of characters
The ```split``` function splits 
```
words = "this is a test".split()
columns = "10,25,hello,1.0".split(',')
letters = list("abcd")
```



