#this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

#ask the player to guess 6 times
for guessesTaken in range(1, 7):
	print('Take a guess.')
	guess = int(input())

	if guess < secretNumber:
		print('your guess is too low.')
	elif guess > secretNumber:
		print('your guess is to high.')
	else:
		break #correct guess

if guess == secretNumber:
	print('good job! you\'re right fuckface!' + ' you guessed in ' + str(guessesTaken) + ' guesse!')
else:
	print('Nope. you stupid fuck. it was ' + str(secretNumber))
