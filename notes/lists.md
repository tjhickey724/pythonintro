# Lists
A Python list stores a sequence of any Python objects.

## Creating lists
They can be created using square brackets with the Python elements separated by commas, e.g.
``` python
> primes = [2,3,5,7,11,13,17,19]
> articles = ['a', 'an', 'the']
> misc - [0, 'hello', 3.14159, True, 2.718281828]
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

## Accumulation loops
It is very common to uses lists for accumulation.
``` python
poem = ['Two', 'roads', 'diverged', 'in', 'a', 'yellow', 'wood']
long_words=[]
for word in poem:
  if len(word)>=4:
    long_words.append(word)
print(long_words)
```
will print
```
['roads','diverged','yellow','wood']
```
or we can read numbers from the user and store them in a list:
``` python
x=-1
numbers=[]
done=False
while not done:
  x = input("Enter a positive number, 0 to stop: ")
  if x>0:
    numbers.append(x)
  else:
    done=True
print('you entered',numbers)
print('the average is',sum(numbers)/len(numbers))
```

  
