from random import randint

def play_game(n):
    ''' generate a number in range 0 to n, and ask user to guess it '''
    answer = randint(0,n)
    guess = -1
    print('guess a number between 0 and',n)
    while guess != answer:
        guess = int(input("Make a guess: "))
        if guess > answer:
            print("Your answer is too high")
        elif guess < answer:
            print("Your guess is too low")

    print("You got it!")
    print('done')

play_game(100)