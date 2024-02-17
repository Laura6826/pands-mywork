# Lab 4.2.3. Guess3.py
# The aim of this program is to promt the user to guess a number until the correct answer is reached.
# Author: Laura Lyons

x= 21
guess = int(input('Please enter a number: '))
while guess != x:
    if guess<x:
        print ('Your guess is too low, please try again')
    elif guess>x:
        print ('Your guess is too high, please try again')
    guess= int(input( 'Please guess again: '))

print ('Well done! {} was the correct number!'. format(guess))