# String Operations

## String functions
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
You can repeatedly concatenate lists with multiplication, e.g.
``` python
> print('etc, '*5)
etc, etc, etc, etc, etc,
> print("*'*10)
**********
```
You can test if one string is a substring of another with "S in T"
``` python
def is_vowel(x):
   return x in "aeiou"
def is_substring(s,t):
   return s in t
```

## String methods
Python also has many builtin string methods, including the following
``` python
capitalize, casefold, center, count, encode, endswith, expandtabs, 
find, format, format_map, index, 
isalnum, isalpha, isascii, isdecimal, isdigit, isidentifier, islower, isnumeric, isprintable, isspace, istitle, isupper, 
join, ljust, lower, lstrip, maketrans, partition, 
removeprefix, removesuffix, replace, rfind, rindex, rjust, rpartition, rsplit, rstrip, 
split, splitlines, startswith, strip, swapcase, title, translate, upper, zfill
```
You can use the ```help(...)``` method to get documentation about these. Some of the most useful ones are
* ```A.startswith(B)```  returns true if the string A starts with the string B, (i.e. B is a prefix of A), e.g.
    * ``` "python".startswith("py") --> True ```
* ```A.endswith(B)``` returns true if the string A ends with the string B, (i.e. B is a suffix of A)
* ```A.lower()``` returns the lowercase version of A, e.g. 
    * ``` "HeLLo".lower() -> "hello" ```
* ```A.upper()``` returns the uppercase version of A
* ```A.capitalize()``` returns a capitalized version of A, e.g. 
   *  ``` "allWoRDs".capitalize() -> 'Allwords' ```
* ```A.strip()``` removes any white space before and after the word, so 
   *  ``` "  \t abc \n ".strip() -> "abc" ```
* ```A.index(B)``` returns the index where substring B first appears in A (and -1 if it doesn't appear)
   *  ```A.index(B,start,end)``` returns the first index of B in A with start<=index<finish
   *  ```A.rindex(B,[start, end])``` returns the right most index of B (possibly restricted to A[start:end])

We'll look at more of these later, e.g. split, format, and replace.

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
```
If you omit the START index then it will start at the beginning of the string

If you omit the END index, then it will end at the end of the string

For example,
``` python
> x="abcdefg"
> print(x[:3])
abc
> print(x[3:])
defg
> print(x[:])
abcdefg
```

## String Accumulation Loops
We can transform one string into another using a string accumulation loop.
For example, the remove all of the vowels from a string we can use the following loop.
``` python
sentence = input("Enter a sentence: ")
new_sentence = ""
for letter in sentence:
    if not letter in "aeiou":
        new_sentence += letter
print(new_sentence)
```

## Spitting a string into a list of words
We can use the L.split(S) method to split the string L into a list of strings using the separator string S, e.g.
We can analyze the short poem, The Purple Cow by Gelett Burgess as follows:
``` python
poem = '''I never saw a Purple Cow,
I never hope to see one,
But I can tell you, anyhow,
I'd rather see than be one!'''
lines = poem.split('\n') # same as poem.split(',') for this poem
words = poem.split(' ')  # same as poem.split()
phrases = poem.split(',')
line1_words = lines[0].split()
print(line1_words)
```
will print
``` python 
['I', 'never', 'saw', 'a', 'Purple', 'Cow,']
```
