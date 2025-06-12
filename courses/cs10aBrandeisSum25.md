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

## L07: Mon 6/16/2025 Review and Practice

Today we review and get more practice.
In particular we look at ways of structuring programs using functions.

---

## L08: Tue 6/17/2025 Strings
Today we cover
[Chapter 8: Strings](https://openstax.org/books/introduction-python-programming/pages/8-introduction)

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 7: Strings__ of the Zybook and complete all of the exercises and labs in Chapter 7.
Submit a reflection about what you learned on the MLA app.

### Additional Notes:
* [reading from a file](../notes/files.md)
* [text processing](../notes/text_processing.md)
* [Eliza and Chatbots](../notes/chatbots.md)

---

## L09: Wed 6/18/2025  Lists
Today we cover
[Chapter 9: Lists](https://openstax.org/books/introduction-python-programming/pages/9-introduction)

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
Today we cover 
[Chapter 7: Modules](https://openstax.org/books/introduction-python-programming/pages/6-introduction)
of the OpenStax textbook.

**Zybook Homework due Tomorrow:** 
Read __Zybook Chapter 11: Modules__ of the Zybook and complete all of the exercises and labs in Chapter 11.
Submit a reflection about what you learned on the MLA app.



---

## L11: Tue 6/24/2025  Dictionaries and Data Representation
Today we discuss
[Chapter 10: Dictionaries](https://openstax.org/books/introduction-python-programming/pages/10-introduction)
### Additional Notes:
* none

---

## L12: Wed 6/25/2025 Multidimensional Arrays

---

## L13: Thu 6/26/2025 Review and Practice

---

---

# Week 5: Object Oriented Programmin in Python

---

## L14: Mon 6/30/2025 Classes and Object Oriented Programming in Python

---

## L15: Tue 7/1/2025

---

## L16: Wed 7/2/2025

---

## L17: Thu 7/3/2025

---



