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
