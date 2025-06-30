# CS10a: Introduction to Problem Solving in Python
## Summer 2025, Brandeis University, 
## Instructor: Tim Hickey 
## [Resources](../notes/python_environments.md) - texts, environments, LLMs
---
## Textbooks

* zybook: CS10a Introduction to Problem Solving in Python -- **required for assessment**
 
* [OpenStax.org: Introduction to Python Programming](https://openstax.org/details/books/introduction-python-programming) optional free online textbook which we will use during the lessons

---
## Learning Objectives for the course
By the end of the course you should be able to
* read short Python programs (< 100 lines) and explain what happens when you run the program
* write short Python programs (< 100 lines) to meet an explicit set of specifications
* write short Python programs to solve some problem you find interesting
* use LLMs (e.g. gemini.google.com) to
  - create Python programs, and
  - explain how they are working, and
  - learn about new features of Python
* run Python programs in VScode and in Google Colab as well as in PyTutor and Brython

---

## Flexible Deadlines
This course has flexible deadlines. If you can't make the deadline then send me an email explaining when you will get it done. I strongly encourage you to use some effective Time Management tools such as
* Pomodoros
* the 5 second rule
* Calendaring

You can learn more about these techniques by watching the videos on this link
[time management tips](https://docs.google.com/document/d/1LVNXHE6NiL_NKLMpGiK4iXbyRGOXyC6D/edit?tab=t.0)

---

## Programming Projects -- due each Monday
The goal of the programming projects is to assess your ability to write
and understand python programs.
The weekly projects consist of 2 types of programming assignments:
* a lab assignment where you show you can use the concepts you learned to solve a problem given by the instructor
* a creative assignment where you show you can use the concepts you learned to solve a problem of your own creation

For both assignments you will need to submit the python code and it should contain a comment at the top with your name and email and links to two short movies (2 minutes each). 
* The first movie shows you running the program and explanining what it does and why its answers are correct.
* The second movie show you explaining how the code works.

For each assignment, there will be more information about what the 2 movies should contain. The goal here is for you and the instructor to validate that you have mastered the skills needed to write and understand programs using the features we have learned up to that point.  

If your videos do not clearly show that you fully understand the features used in your programs, then you'll be asked to meet on Zoom with the instructor or a TA, to review the key concepts. You may be asked to make revisions to your code and to resubmit new videos.... 

---

---

# Week 1: Straight-line programs 

---

## Week 1 Programming Projects (due Monday 6/9/25)
* [PA1](../projects/pa1) Programming Projects and Videos for Week 1

---

## L01: Wed 6/4/2025  -- Variables, Expressions, and Environments
Today we 
* review the syllabus and
* discuss the learning objectives for the course
* practice writing and running simple Python programs in Brython and Python Tutor
* cut/paste our answers into the Mastery Learning App and review each others answers.
 
We spend most of the lesson learning how to write straight-line programs from 
[Chapter 1: Statements](https://openstax.org/books/introduction-python-programming/pages/1-introduction)
of the OpenStax text.

You can attend the class synchronously (in real time) or asynchronously (watching the screen recordings),
but in either case you need to answer questions posed in class using the Mastery Learning App as these
count toward your final grade.

**Zybook Homework due Tomorrow: PA1/ZP1** 

Read __Zybook Chapter 1:Introduction to Python__ of the Zybook and complete all of the exercises and labs.
Submit a reflection about what you learned on the MLA app. You can use gemini to help you with the labs, but use it in a way that helps you learn, not just to complete the assignments...


## Additional notes
* [python environments](../notes/python_environments.md)
* [printing strings](../notes/printing_strings.md)
* [variable-naming](../notes/variable_naming.md)
* [Python Arithmetic](../notes/python_arithmetic.md)
* [Variables](../notes/variables.md)
* [Input](../notes/input.md)

---

## L02: Thu 6/5/2025 -- Expressions

__NOTE__ I don't have office hours today...

Look at Zybooks analytics
* about half of class has completed the Ch1 problems
* the average time is about 1 hour

Today we cover 
[Chapter 2: Expressions](https://openstax.org/books/introduction-python-programming/pages/2-1-the-python-shell)
in the OpenStax text. We will do some of the problems in the openstax book answering the
question on the Mastery Learning App.

### Concepts covered
* variables as named locations in memories
* strings, ASCII, and Unicode
* expression evaluation by looking up values in memory
* variable assignment as storing values in memory using PEMDAS
* compound operators ``` x += 4    y *= x    x *= x   z /=2 ...```
* tracing straightline programs by hand (being a pythontutor clone!)
* variable naming, python keywords, python builtins, ```dir() dir(__builtins__)```
* types and the ```type(x)```  function and the ```id(x)``` function
* type conversion: ```int(x), float(x), str(x)```
* scientific notation ```6.022e-23 = 6.024 * 10^(-23)```
* overflow and underflow ```2.0 ** 10000 == inf``` ```2.0 ** (-10000 == 0```
* operations on mixed data types:  int * float, str * int, str + float, int / int
* roundoff errors and the ```round(x)``` function
* integer division ```x//y``` and modulo ```x%y```
* importing the math module ```math.sin(x)  math.pi math.ex(x) math.log(x) ...```
* importing the random module ```random.random(), random.randint(a,b)```
* formatting code with blank lines

**Zybook Homework due Monday:** 
Read __Zybook Chapter 2: Variables and Expressions__ of the Zybook and complete all of the exercises and labs in Chapter 2.
Submit a reflection about what you learned on the MLA app.

**MLA Homework due Monday:**
* CP1 - create a custom calculator and 2 movies
* LP1 - create the Amortization calculator and 2 movies
  - we can try the 7 step approach to problem solving for this...

### Additional notes
* [problem solving strategy](../notes/problem_solving.md)

---

--- 

# Week 2: Objects, Conditionals, Loops

---

## Week 2 Programming Projects (due Monday 6/16/2025)
* [PA2](../projects/pa2) Programming Projects and Videos for Week 2

---

## L03: Mon 6/9/2025 Objects and Types
Today we cover 
[Chapter 3: Objects](https://openstax.org/books/introduction-python-programming/pages/3-introduction)
of the OpenStax textbook and of the Zybook

We begin by looking over some of the creative homeworks that were due today
and we talk about the new form for requesting a homework deadline extension.

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 3: Types__ of the Zybook and complete all of the exercises and labs in Chapter 3.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [setup the vscode environment](../notes/vscode.md)
* [string operations](../notes/string_operations.md)
* [lists](../notes/lists.md)
* [tuples](../notes/tuples.md)
* [sets](../notes/sets.md)
* [dictionaries](../notes/dictionaries.md)


---

## L04: Tue 6/10/2025  Conditionals
Today we finish up our discussion of Objects then we cover 
[Chapter 4: Decisions](https://openstax.org/books/introduction-python-programming/pages/4-introduction)
of the OpenStax textbook. 

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 4: Branching__ of the Zybook and complete all of the exercises and labs in Chapter 4.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [conditionals](../notes/conditional_execution.md)

---

## L05: Wed 6/11/2025  Loops
Today we cover
[Chapter 5: Loops](https://openstax.org/books/introduction-python-programming/pages/5-introduction)
of the OpenStax textbook

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 5: Loops__ of the Zybook and complete all of the exercises and labs in Chapter 5.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [while loops](../notes/while_loops.md)
* [for loops](../notes/for_loop_basic.md)
* [ranges](../notes/range.md)
* [for loops and lists](../notes/lists2.md)

---
  



## L06: Thu 6/12/2025 Functions

Today we cover
[Chapter 6: Functions](https://openstax.org/books/introduction-python-programming/pages/6-introduction)
of the OpenStax textbook

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 6: Functions__ of the Zybook and complete all of the exercises and labs in Chapter 6.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [simple functions](../notes/functions_basic.md)
* [refactoring](../notes/functions_refactoring.md)
* [functions with parameters](../notes/functions_parameters.md)
* [functions returning values](../notes/functions_returning_useful_values.md)
* [whether to use return or print in a function](../notes/functions_return_vs_print.md)


### Additional Notes:
* [scope of variables in functions](../notes/functions_scope_of_variables.md)
Today we get more practice with analyzing Python programs.
---

---

# Week 3: Functions, Strings, and Lists

NOTE:  class on Tuesday is rescheduled for Thursday.
Since Thursday is a holiday you don't have to attend and can watch
the video instead, but I will be on Zoom as usual. I have a medical
procedure on Tuesday and so can't make it.

## L07: Mon 6/16/2025 Review and Practice

Today we review and get more practice.
First we complete our review of the Functions chapters,
then we look at ways of structuring programs using functions.

Our approach is to
1. solve the problem by hand
   * with person A simulating the computer
   * with person B acting as the user
   * and  person C writing everything down as a transcript
2. convert the transcript to pseudocode
3. convert the pseudocode to python and test it

In part (3) we do this using "stub" functions.

### Examples
1. program to guess a number between 1 and N
2. program to play hangman with a user
3. program to play wordle

---

## Tue 6/17/2025 Class Rescheduled for Thursday 6/19


## L08: Wed 6/18/2025 Strings
First we go over the debugging of the Hangman game..

Then we cover
[Chapter 8: Strings](https://openstax.org/books/introduction-python-programming/pages/8-introduction)
and we look at how to read a set of words from a file into a list of words (which we can use for the hangman game).

Then we look at the Eliza chatbot example and discuss the L3b Chatbot homework problem..

Then we use the same process we applied for hangman to write a wordle program...

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 7: Strings__ of the Zybook and complete all of the exercises and labs in Chapter 7.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [reading from a file](../notes/files.md)
* [text processing](../notes/text_processing.md)
* [Eliza and Chatbots](../notes/chatbots.md)

---

## L09: Thi 6/19/2025  Lists  (Juneteenth, attendance is optional)

First, we cover a little more detail on lists and dictionaries ...
[Chapter 9: Lists](https://openstax.org/books/introduction-python-programming/pages/9-introduction)

Then we brainstorm a little about possible ideas for an interactive game for homework CP3
and type our ideas 
[here](https://docs.google.com/document/d/1sjKWG1xGSEdZri5yFKCCRwTxv9nwq6maAxAVtYHhWQI/edit?usp=sharing)

Next, we show how to write a program to play the wordle game with a user.
[Here](https://wordleunlimited.org) is a website for playing wordle.

We write this program in the same way that we wrote the hangman game... 
1. play the game with a person being the computer and explaining out loud every thing they are doing
  write down what they said
2. convert the transcript into pseudocode
3. convert the pseudocode into code using stub functions with good docstrings
4. write the bodies of the stub functions and test them. We will use AI to help us do this, and to explain it!
5. test the entire program and walk through it with the debugger... 

We will do 1,2,3 and part of 4. Your homework is to complete 4 and do 5....

Time permitting we will start our exploration of Python for Data Science.
We start by adding some information to 
[this google spreadsheet](https://docs.google.com/spreadsheets/d/1xAA0AE6P5Fu2IjAcq5Fq4fMfWlK-JMFUb3CcOHyd2_g/edit?usp=sharing)
Then we download the spreadsheet as a csv file and show how to start analyzing it using Python.

The first step is to using the csv package to read it as a list of dictionaries.
Then we can use Comprehensions to analyze the data.

Time permitting we will look at a real-life data set consisting of Brandeis course data from 2021-2022 available at
[this link](https://drive.google.com/file/d/1f5ClJDNWqwh-gFlgvnwJASIYJOGyBYwy/view?usp=sharing)






**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 8: Lists and Dictionaries__ of the Zybook and complete all of the exercises and labs in Chapter 8.
Submit a reflection about what you learned on the MLA app.

### Additional notes:
* [accumulation loops](../notes/accumulation_loops.md)
* [comprehensions](../notes/comprehensions.md)


---

---

# Week 4: Data Science in Python

---

## L10: Mon 6/23/2025 | Modules
We begin by looking over the creative assignments from week 3 and commenting on them.

Next, we begin by working on the Pokemon Battle app from last time and we work together to refactor it using functions.
Refactoring is an important skill to develop.  We can also ask our AI to refactor the program, but it is good to
do it ourselves so we understnd what is happening.

Next, we cover 
[Chapter 7: Modules](https://openstax.org/books/introduction-python-programming/pages/7-introduction)
of the OpenStax textbook, and we create a module for working Pokemon. This could be used for lots of different
Pokemon style games... The pokemon are represented using lists of dictionaries.
[Chapter 10: Dictionaries](https://openstax.org/books/introduction-python-programming/pages/10-introduction)

This is an example of refactoring a program into multiple files which can make the code more useful as it can
be used for multiple different programs.

Here is the file [monsters.py](https://github.com/tjhickey724/pythonintro/blob/main/code/pokemon/monsters.py)
containing our monsters!

``` python
monsters = [
    {
      "name": "Charmander",
      "health": 100,
      "attacks": [
        {"name": "Scratch", "min_damage": 15, "max_damage": 25},
        {"name": "Ember", "min_damage": 10, "max_damage": 30}
      ]
    },
    {
      "name": "Squirtle",
      "health": 90,
      "attacks": [
        {"name": "Tackle", "min_damage": 10, "max_damage": 20},
        {"name": "Water Gun", "min_damage": 15, "max_damage": 25}
      ]
    },
    {
      "name": "Bulbasaur",
      "health": 110,
      "attacks": [
        {"name": "Vine Whip", "min_damage": 12, "max_damage": 22},
        {"name": "Razor Leaf", "min_damage": 8, "max_damage": 35}
      ]
    },
    {
      "name": "Pikachu",
      "health": 85,
      "attacks": [
        {"name": "Quick Attack", "min_damage": 18, "max_damage": 28},
        {"name": "Thunder Shock", "min_damage": 13, "max_damage": 32}
      ]
    }
  ]
```
**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 11: Modules__ of the Zybook and complete all of the exercises and labs in Chapter 11.
Submit a reflection about what you learned on the MLA app.

Read __Zybook Chapter 22: Additional Labs on Loops__ of the Zybook and complete all of the exercises and labs in Chapter 22.
Submit a reflection about what you learned on the MLA app.



---


## How to succeed in this course 
Your course grade is based on the number of skills you master. 

This course has 12 zybook chapter skills (Ch1--Ch12)
and 4 zybook Additional Lab skils (Ch22-25) and we will add a few more next week
So there will be about 20 zybook skills. Each of these skills has a required reflection, but
you also need to answer all of the questions in the zybook for those chapters...

There are 4 creative programming skills CP1,CP2,CP3,CP4
and there are 5 lab programming skills LP1, LP2a, LP2b, LP3a, LP3b
There is one participation skill PART which is the proportion of participation questions you answer with a good faith effort.
That sums to 30 skills.

If you master S skills then your grade will be 10 + 3*S,
so you get 10 points for fee and 3 points for each skill.

We will cover object oriented programming next week (Python classes and exceptions)
on Monday and Tuesday, but there is no class on Wednesday or Thursday as those are for final
exams and we don't have any final exams. So you can use that time to complete as many of the skills
as you can.

All course work needs to be submitted by Thursday 7/3/2025 before midnight
This is the only hard deadline in the course, and it can be extended because I have
a very full schedule for the rest of the summer that I can't change.

Please come to our office hours to get help if you need it, and also ask gemini or another AI for help,
but double check its answers as it can confidently give wrong answers!

---


## L11: Tue 6/24/2025  Dictionaries and Data Representation

We begin by reviewing what you need to do to succeed in this course.

Then we continue with the pokemon example and show how to move some of the code into a module
that we can then import into the game program.  This breaks the code into two files in a nice way
and further simplifies the structure and organization of the program, making it easier to understand,
modify, and maintain.

Next,we start doing data science with large lists... and we look at several lists:
* US baby names from 1880-2020 with
  [this jupyter notebook](https://github.com/tjhickey724/pythonintro/blob/main/code/jupyter/baby100.ipynb)
* the full list of Brandeis courses during the 21-22 academic year... with
  [this jupyter notebook](https://github.com/tjhickey724/pythonintro/blob/main/code/courses/courses.ipynb)
* colab data sets
We also show how to use the numpy and matplotlib libraries for creating visualizations.

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 12: Files__ of the Zybook and complete all of the exercises and labs in Chapter 12.
Submit a reflection about what you learned on the MLA app.

Read __Zybook Chapter 23: Additional Labs on Functions__ of the Zybook and complete all of the exercises and labs in Chapter 23.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* none

---

## L12: Wed 6/25/2025 Multidimensional Arrays

Today we look at storing data as a table of values,
e.g. a color photo is a table of tuples (r,g,b) where
r,g,b are the amounts of red, green, and blue in the pixel 
at that location (row i and col j).

We explore photo manipulation using jupyter notebooks in google colab
following [this tutorial](https://github.com/tjhickey724/pythonintro/blob/main/code/pa04_images/images.ipynb)

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 24: Additional Labs on Strings__ of the Zybook and complete all of the exercises and labs in Chapter 24.
Submit a reflection about what you learned on the MLA app.

---

## L13: Thu 6/26/2025 Review and Practice

Grading update... I've decided to only assign Ch9 and 10 next week and no more additional
labs, so there will be 26 total skills and your grade will be
22 + 3*S where S is the number of skills you master (with participation being 1 skill)

Next week we cover Python Classes and Exceptions on Monday and Tuesday.
I'll hold office hours on Wed and Thu to help everyone complete their homework
All the homework is due by Thursday 7/3 before midnight. 

We first brainstorm about ideas for the CP4 homework at this link:
https://docs.google.com/document/d/1vvQqo-90Da6Z5Yn4JpAi87bPw9KDGG3S0kaM3XRodbs/edit?tab=t.0

In the first hour, we continue with the image manipulation and explore and write functions 
* to convert an image to black and white
* to convert an image to use fewer colors
* to merge two images.
* to implement a green screen effect
* to detect edges

In the second hour, we get more practice with basic python programming using problems from 
[codingbat.com](https://codingbat.com/python) and other places. We will also look at some problems from
[Project Euler](https://projecteuler.net/archives) for those who like Mathematical problems.

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 25: Additional Labs on Lists and Dictionaries__ of the Zybook and complete all of the exercises and labs in Chapter 25.
Submit a reflection about what you learned on the MLA app.

---

---

# Week 5: Object Oriented Programmin in Python

---

## L14: Mon 6/30/2025 Classes and Object Oriented Programming in Python

This is the last week of class. There is no class on Wed or Thu, but I will have open office hours
if you want to stop by for some help. Thu 7/3 is the last day to submit work for this class. 
Please try to complete all of the Zybook chapters (and write a reflection on the Mastery App)
and complete all of the creative and lab problems on the Mastery App.

Today we introduce classes and we go through the 
[Official Python Tutorial on Classes](https://docs.python.org/3/tutorial/classes.html#)
and we'll look at the [OpenStax chapter on Classes](https://openstax.org/books/introduction-python-programming/pages/11-introduction)


**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 9: Classes__ of the Zybook and complete all of the exercises and labs in Chapter 9.
Submit a reflection about what you learned on the MLA app.

You can get 1 extra credit skill by completing 
[this survey reflecting on your experience in this course](https://docs.google.com/forms/d/e/1FAIpQLSdZNjx4GK3PjVmJxq46N45eSQHPoXBWmgKPVDYUQ8VqltBZqw/viewform?usp=preview)

---

## L15: Tue 7/1/2025  Sorting and Recursion

We talk about sorting algorithms and implement [mergesort](https://github.com/tjhickey724/pythonintro/tree/main/code/merge_sort) as a recursive algorithm.

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 10: Exceptions__ of the Zybook and complete all of the exercises and labs in Chapter 10.
Submit a reflection about what you learned on the MLA app.

---

## L16: Wed 7/2/2025
FINAL EXAMS - no exams in this class, so you can work on your final creative project

---

## L17: Thu 7/3/2025
FINAL EXAMS - no exams in this class, so you can work on your final creative project

---



