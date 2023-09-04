'''
Number Guessing Game In python
This beginner Python project is a fun
 game that generates a random
 number (in a certain range) that the
   user must guess after receiving hints.
     For each wrong guess the user makes, 
     they receive extra hints, but at the 
     cost of reducing their final score. It only needs knowledge on 
     1. Built in python random module
     2. Use of conditional operators like if and loop 
     3. String formating 
    
     Hello you can support me by checking on my social handles 
     https://twitter.com/binaryCodeStar
     
-------------------------------------------------------------
'''

import random

attempts_list = []


def show_score():
    if not attempts_list:
        print('There is currently no high score,'
              ' it\'s yours for the taking!')

    else:
        print(f'The current high score is'
              f' {min(attempts_list)} attempts')


def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s  Greater')
                elif guess < rand_num:
                    print('It\'s Lower')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()
