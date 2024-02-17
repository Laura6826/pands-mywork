# Lab 4.2.2. Guess1.py
# The aim of this program is to promt the user to guess a number until the correct answer is reached.
# Author: Laura Lyons

x= 21
guess = int(input('Please enter a number: '))
while guess != x:
    print ('Wrong number, try again!')
    guess= int(input( 'Please guess again: '))

print ('Well done! {} was the correct number!'. format(guess))