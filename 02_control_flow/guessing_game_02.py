"""Importing the random module and using the randint() function"""
import random
upper_limit = 10
answer = random.randint(1, upper_limit)

print("Please guess a number between 1 and {}: ".format(upper_limit))
guess = int(input())

if guess < answer:
    print('Too low. Guess again: ')
    guess = int(input())
    if guess == answer:
        print('Well done! You guessed it!')
    else:
        print('Sorry. Wrong again. \nThe correct answer was {}'.format(answer))
elif guess > answer:
    print('Too high. Guess again: ')
    guess = int(input())
    if guess == answer:
        print('Well done! You guessed it!')
    else:
        print('Sorry. Wrong again.\nThe correct answer was {}'.format(answer))
else:
    print('You got it correct on your first try! \nThe number was ' + str(guess) + '!')
