import random
with open('code/words5.txt','r') as file:
    words = file.read().split()
    print('the number of words is',len(words))

def play_wordle():
    word = random.choice(words)
    print('the word is',word)
    guess = input('guess a word: ')
    guess_count = 0
    guesses_remain = 6
    while guess != word and guesses_remain>0:
        print('wrong')
        guess_count += 1
        guesses_remain -= 1
        print('Your total guesses are:', guess_count)
        print('You have this many guesses left:',guesses_remain)
        guess = input('guess a word: ')
    print('correct')


play_wordle()
