"""Convert guessing game to use a while loop"""
import random
upper_limit = 10
answer = random.randint(1, upper_limit)
print(answer)
print("Please guess a number between 1 and {}: ".format(upper_limit))
guess = int(input())
while guess != answer:

    if guess < answer:
        print('Too low. Guess again: ')
        guess = int(input())
    elif guess > answer:
        print('Too high. Guess again: ')
        guess = int(input())
print('You got it correct! \nThe number was ' + str(guess) + '!')
