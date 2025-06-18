# Chatbots
The simplest chatbot is a program that prompts the user for a sentence, then responds, and 
continues until the user wants to quit.  ChatGpt uses a sophiticated algorithm to come up with
responses, but we can create a simple chatbot that uses canned responses.  

Here is a link to a simple chatbot, [eliza.py](https://github.com/tjhickey724/pythonintro/blob/main/code/eliza.py)
which simulates a psychiatrist. 

The top level code for elize.py is the following::
```
def talk_with_eliza():
    ''' main loop - prompt user and generate responses '''
    user_input = input("eliza: How are you doing today?\n> ")
    while user_input != 'goodbye':
        words = user_input.split()
        computer_response=generate_response(words)
        user_input = input('eliza: '+computer_response+"\n> ")
    print('bye')
```

The main functionality of this program is the generate_response function defined as follows:
``` python
def generate_response(user_words):
    ''' generates random responses based on the user's response '''
    if intersects(user_words,sad_words):
        return choice(sad_responses)
    if intersects(user_words,work_words):
        return choice(work_responses)
    elif len(user_words)<2:
        return choice(short_responses)
    else:
        return choice(generic_responses)
```
This uses the "intersects" function whose arguments are two lists of words, and which returns true if those lists have a word in common:
``` python
def intersects(list1, list2):
    ''' return true if list1 and list2 contain a common element '''
    for word in list1:
        if word in list2:
            return True
    return False
```
The idea here is to look for certain key words (like sad words such as _sad depressed blue down upset crying_
and if the user's statement contains any of those, then to randomly pick a response from a list of sad_responses.
Here we use the library function ```choice``` which returns a randomly selected member of a list.
``` python
sad_words = "sad depressed blue down upset crying".split()
sad_responses = [
    "I'm sorry to hear that.",
    "Who can you talk to when you are sad?",
    "What is making you feel sad?",
    "Do you often feel depressed?",
    ]
```


