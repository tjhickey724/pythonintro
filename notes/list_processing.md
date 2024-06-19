# List Processing

There are three common operations that we perform on lists and we'll discuss them in this note.
* reduction - processing all elements of a list and producing some summarization (e.g. number of elements in the list of a certain type)
* mapping - applying some function to every element of a list to create a new list
* filtering - applying a test to every element of a list and creating a list of those elements that passed the test.

Python has a special syntax producing lists using mapping and filtering (called *comprehensions*) but it is good to know
how to do this directly, which is what we'll focus on first.

## Accummulation loops
These are loops that produce some kind of summary statistic for a list, for example the smallest number in a list, or the sum of the numbers in a list, or the number of short words in a list of words.
These programs all have the same basic pattern shown below:
``` python
result = ...starting value...
for item in list_of_items:
    update result based on the item
```
For example, to find the sum of the numbers is in a list of numbers we would use
``` python
numbers = list(range(1,1000))
result = 0
for num in numbers:
    result = result + num
print(f'The sum from 1 to 1000 is {result}')
```
or to find the length of the longest word in a sentence
``` python
words = "Now is the time for all good men to come to the aid of their country"
result = 0
for word in words:
   if len(word)>result:
        result = len(word)
print(f'the longest word in the sentence has length {result}')
```
