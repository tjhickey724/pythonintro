# Sets
A python set is an unordered collection of "hashable" elements with no duplicate elements.
Hashable means that it is immutable (e.g. a tuple) and all of its elements are also hashable.
Typical sets are made from strings, numbers, and tuples of strings and numbers.

## Creating sets
Sets are created using the curly brace notation {}
``` python
s = {2,3,5,7,11,13}
t = {'hi','hello','howdy','hola','konichi-wa'}
z = {(1,6), (2,3), (3,2), (6,1)}
```

## Converting between sets and lists (and tuples)
Sets can also be created from lists (or tuples) using the ```set(L)``` function
``` python
nums = [3,1,4,1,5,9,2,6,5,3,5]
digits = set(nums)  # assigns the set {3,1,4,5,9,2,6} to digits
```
Observe that when we converted the list to a set, it removed the duplicate elements but didn't sort it.

You can convert a set into a list using ```list(s)``` or ```sorted(s)```
``` python
ds = sorted(digits) # assigns the list [1,2,3,4,5,6,9] to ds
```
likewise ```tuple(s)``` will convert a set into a tuple

## Set operations
You can test if something is in a set using ``` x in s``` just as with lists and tuples
but you can not use indexing or slicing on a set
```
digits = set(list(range(0,10)))
digits[4]  # RAISES AN ERROR
digits[2:8] # RAISES AN ERROR
```
If you want to use indexing or slicing first convert the set ```s``` into a list ```vals = list(s)```

You can also create new sets using the set operations 
``` pythons
s_or_t = s | t  # s_or_t is the set of all elements in s or in t
s_and_t = s & t  # s_and_t is the set of elements in s and in t
s_diff_t = s-t  # s_diff_t is the set of elements in s and not in t
s <= t  # this is true if s is a subset of t, i.e. everything in s is also in t
len(s) # returns the number of elements in s
s.add(x) # adds the element x to the set s
s.remove(x) # removes the element x from the set s, generates error if x is not in s
```






