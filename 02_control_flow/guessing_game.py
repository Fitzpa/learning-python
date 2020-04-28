"""Create a guessing game without actually creating any functions.
This will end up being very repetive and is just an example of nesting if else statements"""

answer = 5

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print('Too low. Guess again: ')
    guess = int(input())
    if guess == answer:
        print('Well done! You guessed it!')
    else:
        print('Sorry. Wrong again.')
elif guess > answer:
    print('Too high. Guess again: ')
    guess = int(input())
    if guess == answer:
        print('Well done! You guessed it!')
    else:
        print('Sorry. Wrong again.')
else:
    print('You got it correct on your first try! \nThe number was ' + str(guess) + '!5')
