# Text Processing
In these notes we explore how to use Python to analyze a large textual dataset, for example a novel or play or research article.

## Prepare the text file
The first step is to find the text and convert it to a ".txt" file 
These files consist of a sequence of characters but with no fonts, highlighting, formating, etc.
A good source of text files is [Project Gutenberg](https://www.gutenberg.org/).
You can download files which are out of copyright in a number of different formats, but
the one we want to analyze with Python is the "Plain Text" format.

For example, here is a link to the [Plain Text version of Frankenstein](https://www.gutenberg.org/ebooks/84.txt.utf-8)

Let's download this file and store it in the folder we are using for our vscode projects.
You can download it by selecting the "Save As" option in the File menu. Let's store it in the file "frankenstein.txt"

## Cleaning the data
Whenever you work on a data set, the first step after downloading it is to prepare it for processing, also known as "cleaning the data".
In this case, the Project Gutenberg text has a prologue and an epilogue that are appended to the the text we're interested in.

The Prologue has meta-data and the Epilogue has information about how you can share this data.

The Prologue for this particular file (as of 6/20/2024) is
```
The Project Gutenberg eBook of Frankenstein; Or, The Modern Prometheus
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: Frankenstein; Or, The Modern Prometheus

Author: Mary Wollstonecraft Shelley

Release date: October 1, 1993 [eBook #84]
                Most recently updated: December 2, 2022

Language: English

Credits: Judith Boss, Christy Phillips, Lynn Hanninen and David Meltzer. HTML version by Al Haines.
        Further corrections by Menno de Leeuw.


*** START OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN; OR, THE MODERN PROMETHEUS ***
```
which ends in the line "*** START OF THE ..."
and likewise, the epilogue begin with a "***" line as follows
```
*** END OF THE PROJECT GUTENBERG EBOOK FRANKENSTEIN; OR, THE MODERN PROMETHEUS ***

Updated editions will replace the previous one—the old editions will
be renamed .....
```
We should load this text file into vscode and delete the prolog and epilogue before
processing (though we could also use Python to do this!!)

We will assume that you have done that and so the file frankenstein.txt contains
only the text of the novel and no meta-data.

You can also do this with any plain text file (e.g. Romeo and Juliet, or a text in any language!)

## Reading in the data as a string
We can read the data into a python variable as a very long string using the following code:
``` python
filename = "frankenstein.txt"
file = open(filename,'r')
text = file.read()
file.close()
```

## Descriptive Analysis
We can easily find the size of the text in characters, words, lines, paragraphs.
For example for characters and words we would do
``` python
print(f'number of characters is {len(text)}')
words = text.split()
print(f'number of words is {len(words)}')
```
How would you find the number of lines (hint: split the text on newlines '\n')
or paragraphs (split on '\n\n')

Likewise, we can find the number of unique word by converting words into a set!
```
unique_words = set(words)
```
How many unique 'words' are in Frankenstein...

Note: this is a little misleading because text.split() uses white space to split the text into "words"
but this will include punctuation, so "help" "help." "help?", "help," and "help!" will all be different words.
To be more precise, we should remove punctuation from the end of words!! How would you do this?

## Creating a concordance
When learning a language is is useful to find all examples of how a word is used.
The list of all occurrences of a word in a text, with context, is called a **concordance**
Let's look at how to build a concordance using Python for a given text.

The main idea is to print all lines of a text that contain a particular word.
Here is the simplest approach
``` python
filename = "frankenstein.txt"
file = open(filename,'r')
text = file.read()
file.close()

lines = text.split('\n')

word = input("What word to you want to look for? ")
for line in lines:
    if word in line:
        print(line)
```
We could also iterate through the indices of the lines:
```
for i in range(len(lines)):
    line = lines[i]
    if word in line:
        print(line)
```
The advantage of this approach is that we could extend it to print the lines before and after the line containing the word

## Coding exercises
* How would you count the number of lines containing a given word?
* How would you print the line number in addition to the line in a concordance?
* How could you print lines containing two different words?
* How can you combine all of the above calculations into one program?





