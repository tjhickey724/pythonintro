'''
computer_guesses.py
is the guessing game where the user picks a random number
and the computer tries to guess in as few guess as possible...

Algorithm  in pseudocode
keep track of the lowest and highest values it could have
lowest =0  highest=100
guess something in the middle, so 50
if 50 is too low, then lowest =50
if 50 is too high, then highest = 50
So we make a guess in the middle, and then adjust either highest or lowest...

What is a reasonable guess to make given lowest and highest???

e.g. lowest=30  highest = 72  guess = midpoint ...

lowest = 0 and highest =100
while didn't guess it ...
   guess = midpoint of lowest and highest
         = lowest + (highest-lowest)//2 = (highest+lowest)//2
   if guess is too low, lowest = guess
   if guess is too high, highest = guess

lowest = 68
highest = 71
guess = 69  
   
'''