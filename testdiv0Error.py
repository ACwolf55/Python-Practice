# Guessing Number Game
import random

print('Hello, What is your name?')
name = input()

print('Well, ' + name + ' I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessTaken in range(1, 7):
    print('take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This is for the correct guess!

if guess == secretNumber:
    print('Good Job ' + name + ' ! You guessed the number in ' + str(guessTaken) + ' guesses')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))


print('You took '+ str(guessTaken) + ' guesses')
