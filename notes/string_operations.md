# String Operations

## Primitive operations
You can find the number of characters in a string using the ```len(s)``` function, e.g.
``` python
> len('hello')
5
```
You can also concatenate two strings using the + operations
``` python
> x = "foot" + "ball"
> print(x)
football
```

## Indexing
Python allows you to access individual elements of a string using an index.
Each character in a string has an index, starting with 0.
You can access an element of a string w using square brackets and the index, e.g.
``` python
phrase = 'hello world'
phrase[0] == 'h'
phrase[1] == 'e'
phrase[2] == 'l'
```


## Negative indices
you can also index from the end of the list
``` python
letters = 'abcdefghijklmnopqurstuvwxyz'
letters[-1] == 'z'
letters[-2] == 'y'
```

## Slices
Python allows you to generate substrings of a string by specifying the start and end of the string
```
word[START:END]
```
where START and END are indices and the substring consists of all characters from index START, up to BUT NOT INCLUDING index END

For example,
``` python
> x = "abcdefg"
> print(x[2:5])
cde
> print(x[
